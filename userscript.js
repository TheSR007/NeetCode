// ==UserScript==
// @name         Copy NeetCode Question in Markdown
// @namespace    TheSR
// @version      1.0
// @description  Adds a copy button to copy question from neetcode.io in Markdown format
// @author       TheSR
// @match        *://neetcode.io/problems/*
// @grant        none
// @run-at document-idle
// ==/UserScript==

(function () {
    "use strict";

    // Function to convert HTML to Markdown
    function htmlToMarkdown(html) {
        let markdown = html;

        markdown = markdown.replace(/<h1[^>]*>(.*?)<\/h1>/g, "# $1\n");
        markdown = markdown.replace(/<h2[^>]*>(.*?)<\/h2>/g, "## $1\n");
        markdown = markdown.replace(/<h3[^>]*>(.*?)<\/h3>/g, "### $1\n");

        markdown = markdown.replace(/<strong[^>]*>(.*?)<\/strong>/g, "**$1**");

        markdown = markdown.replace(/<code[^>]*>(.*?)<\/code>/g, "`$1`");

        markdown = markdown.replace(
            /<pre[^>]*><code[^>]*>([\s\S]*?)<\/code><\/pre>/g,
            "```java\n$1```"
        );

        markdown = markdown.replace(/<p[^>]*>(.*?)<\/p>/g, "$1\n");

        markdown = markdown.replace(/<ul[^>]*>(.*?)<\/ul>/gs, (_, content) => {
            return content.replace(/<li[^>]*>(.*?)<\/li>/g, "- $1\n");
        });

        markdown = markdown.replace(/<br\s*\/?>/g, "\n");
        markdown = markdown.replace(
            /<details[^>]*>\s*<summary[^>]*>([\s\S]*?)<\/summary>\s*<p[^>]*>([\s\S]*?)<\/p>\s*<\/details>/g,
            (_, summary, content) => {
                content = content.trim();
                return `<details>\n<summary>${summary}</summary>\n\n${content}\n\n</details>`;
            }
        );

        markdown = markdown.replace(
            /<(?!\/?(details|summary|strong)\b)[^>]+>/g,
            ""
        );

        return markdown.trim();
    }

    // Function to copy formatted content in Markdown
    function copyToClipboard(button) {
        const contentElement = document.querySelector(
            ".my-article-component-container"
        );
        const difficultyElement = document.querySelector(".difficulty-btn");
        const difficulty = difficultyElement
            ? difficultyElement.innerText.trim()
            : "Easy";
        const difficultyColor =
            difficulty === "Easy"
                ? "green"
                : difficulty === "Medium"
                ? "orange"
                : "red";

        const contentClone = contentElement.cloneNode(true);

        const buttonsToExclude = contentClone.querySelectorAll(
            ".copy-to-clipboard-button"
        );
        buttonsToExclude.forEach(button => button.remove());

        const markdownContent = htmlToMarkdown(contentClone.innerHTML);

        const title = document.querySelector("h1").innerText.trim();
        const formattedContent = `# ${title}\n\n**Difficulty:** <span style="color: ${difficultyColor};">${difficulty}</span>\n\n${markdownContent}`;

        navigator.clipboard
            .writeText(formattedContent)
            .then(() => {
                button.innerText = "Copied!";
                button.style.backgroundColor = "#4caf50"

                setTimeout(() => {
                    button.innerText = "Copy Content";
                    button.style.backgroundColor = "";
                }, 1000);
            })
            .catch(err => {
                console.error("Failed to copy: ", err);
            });
    }

    // Function to add the copy button
    function addButton(targetElement) {
        if (targetElement.querySelector(".copy-to-clipboard-button")) return;

        const button = document.createElement("button");
        button.classList.add("copy-to-clipboard-button");
        button.innerText = "Copy Content";
        button.style.marginLeft = "auto";
        button.style.display = "inline-block";

        targetElement.style.display = "flex";
        targetElement.style.alignItems = "center";
        targetElement.appendChild(button);

        button.addEventListener("click", () => copyToClipboard(button));
    }

    // Function to observe changes in the DOM and reapply the button
    function observePage() {
        const targetNode = document.body;

        const config = { childList: true, subtree: true };

        const callback = function (mutationsList, observer) {
            for (let mutation of mutationsList) {
                if (mutation.type === "childList") {
                    const targetElement = document.querySelector(
                        ".question-tab > div:nth-child(1) > div:nth-child(1)"
                    );
                    if (targetElement) {
                        addButton(targetElement);
                    }
                }
            }
        };

        const observer = new MutationObserver(callback);

        observer.observe(targetNode, config);
    }

    observePage();
})();
