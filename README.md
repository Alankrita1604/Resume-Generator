1. AI Resume Generator — Professional HTML Format

2. Project Overview

Ever wished you could generate a polished, professional resume without all the hassle? This project is an interactive web application built with Streamlit designed to do just that! It cleverly uses the Google Gemini API to craft beautifully styled HTML resumes tailored just for you. Simply input your personal details, education, experience, skills, and even a specific job description, and watch as the AI intelligently formats a modern, two-column resume with clean inline CSS.

3. What It Does

This resume generator is packed with features to make your life easier:

-   Intuitive Interface: Thanks to Streamlit, the data input form is super user-friendly and straightforward.
-   Smart AI Generation: Powered by the Google Gemini API, it doesn't just fill in blanks; it intelligently crafts your resume content.
-   Stunning HTML Output: Get a visually appealing, two-column resume complete with inline CSS, perfect for viewing, sharing, or printing.
-   Tailored Content: Provide a job description, and the AI will adapt your resume content to highlight the skills and experiences most relevant to that role.
-   Clean & Responsive Design: The generated HTML resume is designed to look great and be easily readable across different devices.

4. Technologies Under the Hood

This project is built using a few key technologies:

-   Python: The backbone of the entire application.
-   Streamlit: Our go-to for creating the interactive web interface.
-   Requests: Handles all the communication with the Google Gemini API.
-   Google Gemini API (gemini-1.5-flash): The brains behind the operation, responsible for generating and styling your resume content.

5. Getting Started: Local Installation

Want to run this project on your own machine? Here's how to set it up:

5.1. What You'll Need

-   Python 3.8 or newer.
-   A Google Gemini API Key. If you don't have one yet, you can easily get it from [Google AI Studio](https://aistudio.google.com/app/apikey).

5.2. Installation Steps

1.  Grab the code:
    ```bash
    git clone [Your GitHub Repository URL Here]
    cd [your-repo-name]
    ```

2.  Set up a virtual environment (highly recommended!):
    ```bash
    python -m venv venv
    ```

3.  Activate your new environment:
    -   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    -   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  Install the necessary Python libraries:
    ```bash
    pip install streamlit requests
    ```

5.  Plug in your Gemini API Key:
    Open your main Streamlit file (it's likely named `resume_generator_app.py`) and find this line:
    ```python
    API_KEY = "" #api key added in the document which is uploaded on Prolearn 
    ```
    Replace the placeholder string with your actual Gemini API Key.
    Pro Tip: For real-world applications or deployments, it's much safer to use Streamlit secrets (`st.secrets`) instead of hardcoding your API key directly in the script.

6. How to Use It

Once everything's set up, running the app is simple:

1.  Navigate to your project directory in your terminal (where your `resume_generator_app.py` file lives).
2.  Make sure your virtual environment is active.
3.  Launch the Streamlit app:
    ```bash
    streamlit run resume_generator_app.py
    ```
    (Just remember to swap `resume_generator_app.py` with the actual name of your Python script!)

Your web browser should automatically open the application, usually at `http://localhost:8501`. Go ahead, fill in your details, click "Generate Styled Resume," and see your personalized HTML resume appear!

7. Want to Contribute?

We'd love your help! If you have ideas for improvements, new features, or spot any bugs, please feel free to open an issue or submit a pull request.

Here's a quick guide:

-   Fork the repository.
-   Create a new branch for your changes (`git checkout -b feature/your-awesome-feature`).
-   Make your magic happen!
-   Commit your changes with a clear message (`git commit -m 'Added amazing feature X'`).
-   Push your branch (`git push origin feature/your-awesome-feature`).
-   Open a Pull Request, and let's chat!

8. License

This project is open-source and available under the MIT License. Check out the [LICENSE](LICENSE) file for all the details.
