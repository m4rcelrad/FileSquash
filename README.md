# FileSquash

FileSquash is a lightweight desktop application designed to aggregate multiple source code files from a selected
directory into a single text file. It is specifically built to help developers quickly gather project context to feed
into LLMs.

## Features

* **Easy-to-Use GUI:** A user-friendly interface powered by CustomTkinter.
* **Extension Filtering:** Specify exactly which file types to include.
* **Directory Exclusion:** Ignore specific folders to keep the output clean.
* **Standalone Executable:** Run the tool anywhere without installing Python.

## Download & Usage

If you just want to use the application without dealing with the source code:

1. Go to the **[Actions]** or **[Releases]** tab on this GitHub repository.
2. Download the latest `FileSquash.exe` artifact.
3. Run the executable.
4. Select your target project folder, adjust extensions/exclusions if needed, and click **Squash Files**.
5. Your combined project context will be saved in the selected directory as `project_context.txt`.
