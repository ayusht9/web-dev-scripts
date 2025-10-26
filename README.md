# web-dev-scripts
Helpful scripts related to web development

## Setup for Quick Access

To use this script from anywhere:

1. **Create a folder** to store your utility scripts

   ```bash
   mkdir ~/dev-tools
   ```

   ```cmd
   mkdir %USERPROFILE%\dev-tools
   ```

2. **Move this script** into that folder:

   ```bash
   mv create_web_files.py ~/dev-tools/
   ```

   ```cmd
   move create_web_files.py %USERPROFILE%\dev-tools
   ```

3. **Add the folder to your system PATH** so you can run the script globally:

   * On **macOS / Linux**, add this line to your `~/.bashrc`, `~/.zshrc`, or `~/.profile`:

     ```bash
     export PATH="$PATH:~/dev-tools"
     ```

     Then reload your shell:

     ```bash
     source ~/.bashrc
     ```
   * On **Windows**:

     * Search for “Environment Variables” → “Edit the system environment variables”
     * Click **Environment Variables** → select **Path** → click **Edit**
     * Add the full path to your `dev-tools` folder

4. Now you can run the script from anywhere using:

   ```bash
   python create_web_files.py
   ```
