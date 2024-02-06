# Python Laboratory Codes 3rd Semester B. Tech (Academy Of Technology)
Welcome to the Python repository! This repository contains an introduction to Python. Whether you're a beginner looking to learn or an experienced developer seeking reference implementations, you've come to the right place.


## Installation and Setup

### 1. Python
### Python 3.12 Installation and Setup Guide

Before installing Python 3.12, ensure that your system meets the following requirements:

- Operating System: Windows, macOS, or Linux
- Minimum RAM: 1 GB
- Disk Space: 200 MB for Python installation

#### Steps to Install Python 3.12:

1. **Download Python 3.12:**

   Visit the [Python Downloads](https://www.python.org/downloads/) page and select the appropriate installer for your operating system.

2. **Run the Installer:**

   For Windows, double-click the downloaded `.exe` file and follow the installation wizard prompts. Ensure to check the box that says "Add Python 3.12 to PATH" during installation.

   For macOS and Linux, open a terminal window, navigate to the directory containing the downloaded installer, and run the following command:

   ```bash
   $ sudo ./python-3.12.0-macosx10.9.pkg
   ```

   Replace `python-3.12.0-macosx10.9.pkg` with the name of the downloaded installer file.

3. **Verify Python Installation:**

   After installation, open a terminal or command prompt and enter the following command to verify that Python 3.12 has been installed successfully:

   ```bash
   $ python3 --version
   ```

   You should see an output similar to `Python 3.12.0`.

4. **Update pip (Python Package Manager):**

   It is recommended to update pip to the latest version. Run the following command:

   ```bash
   $ python3 -m pip install --upgrade pip
   ```

#### System Requirements for Python 3.12:

- Operating System: Windows 7 and later, macOS 10.12 and later, Ubuntu 16.04 and later
- Minimum RAM: 1 GB
- Disk Space: 200 MB for Python installation

Follow these steps to install and set up Python 3.12 on your machine. Enjoy coding with Python!

### 2. VS Code

Download and install [Visual Studio Code](https://code.visualstudio.com/). This repository is configured with a `.vscode` folder containing useful settings for your coding environment.

Certainly! Below is an explanation of the commands for forking and contributing to a GitHub repository, formatted for easy copying and pasting:

## Forking the Repository

1. **Fork the repository:** Click the "Fork" button at the top right of the repository page. This creates a copy of the repository in your GitHub account.

   ![Forking](gifs/fork.gif)

2. **Clone your forked repository:** Open your terminal and run the following command to clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/repository.git
   ```

   Replace `your-username` with your GitHub username and `repository` with the name of the repository.

   ![Clone](gifs/clone.gif)

## Contributing

1. **Create a new branch:** Move into the repository directory and create a new branch for your feature or bug fix:

   ```bash
   cd repository
   git checkout -b feature-name
   ```

   Replace `feature-name` with a descriptive name for your contribution.

   ![Branch](gifs/branch.gif)

2. **Make your changes:** Modify the code, add new features, or fix bugs. Once done, stage and commit your changes:

   ```bash
   git add .
   git commit -m "Description of changes"
   ```

   Replace "Description of changes" with a concise and descriptive commit message.

   ![Commit](gifs/commit.gif)

3. **Push to your fork:** Push your changes to your forked repository on GitHub:

   ```bash
   git push origin feature-name
   ```

   Replace `feature-name` with the name of your branch.

   ![Push](gifs/push.gif)

4. **Create a Pull Request (PR):** Go to the GitHub page of your forked repository. GitHub will detect the recent push and display a "Compare & pull request" button. Click on it to create a new pull request.

   ![Pull Request](gifs/pull_request.gif)

   Add a title and description to your pull request, then click "Create Pull Request."

   ![Create Pull Request](gifs/create_pr.gif)

## Points to remember:
- Add only code file i.e .py file



