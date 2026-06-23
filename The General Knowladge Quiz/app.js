// General Knowledge Quiz Application Script

// Quiz Questions Database (3 Questions matching Python / General Theme)
const quizData = [
    {
        question: "What is the capital of France?",
        options: ["London", "Paris", "Rome"],
        correctIndex: 1, // Paris
        explanation: "Paris has been the capital of France since the late 10th century."
    },
    {
        question: "Which planet is known as the Red Planet?",
        options: ["Mars", "Venus", "Jupiter"],
        correctIndex: 0, // Mars
        explanation: "Mars is reddish because of the high concentration of iron oxide (rust) on its surface."
    },
    {
        question: "What is the largest ocean on Earth?",
        options: ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean"],
        correctIndex: 1, // Pacific Ocean
        explanation: "The Pacific Ocean covers more than 30% of the Earth's surface, which is more than all the Earth's land area combined."
    }
];

// App State Variables
let currentQuestionIndex = 0;
let score = 0;
let answerSelected = false;

// DOM Elements
const welcomeScreen = document.getElementById("welcome-screen");
const quizScreen = document.getElementById("quiz-screen");
const resultsScreen = document.getElementById("results-screen");

const startBtn = document.getElementById("start-btn");
const nextBtn = document.getElementById("next-btn");
const restartBtn = document.getElementById("restart-btn");

const questionNumberText = document.getElementById("question-number");
const progressFill = document.getElementById("progress-fill");
const currentScoreText = document.getElementById("current-score");
const questionText = document.getElementById("question-text");
const optionsContainer = document.getElementById("options-container");

const scoreFraction = document.getElementById("score-fraction");
const circleFill = document.getElementById("circle-fill");
const feedbackHeadline = document.getElementById("feedback-headline");
const feedbackDesc = document.getElementById("feedback-desc");

// Event Listeners
startBtn.addEventListener("click", startQuiz);
nextBtn.addEventListener("click", handleNextQuestion);
restartBtn.addEventListener("click", restartQuiz);

// Start the Quiz
function startQuiz() {
    welcomeScreen.classList.remove("active");
    setTimeout(() => {
        welcomeScreen.style.display = "none";
        quizScreen.style.display = "flex";
        setTimeout(() => quizScreen.classList.add("active"), 50);
        loadQuestion();
    }, 400);
}

// Load current question from Database
function loadQuestion() {
    answerSelected = false;
    nextBtn.classList.add("disabled");
    nextBtn.disabled = true;
    nextBtn.innerText = currentQuestionIndex === quizData.length - 1 ? "Finish Quiz" : "Next Question";

    const currentQuiz = quizData[currentQuestionIndex];
    
    // Update headers
    questionNumberText.innerText = `Question ${currentQuestionIndex + 1} of ${quizData.length}`;
    progressFill.style.width = `${((currentQuestionIndex + 1) / quizData.length) * 100}%`;
    currentScoreText.innerText = score;
    
    // Update Question
    questionText.innerText = currentQuiz.question;
    
    // Clear & Populate Options
    optionsContainer.innerHTML = "";
    currentQuiz.options.forEach((option, index) => {
        const optionCard = document.createElement("button");
        optionCard.className = "option-card";
        optionCard.innerHTML = `
            <span>${option}</span>
            <div class="option-indicator">${String.fromCharCode(65 + index)}</div>
        `;
        optionCard.addEventListener("click", () => selectOption(index, optionCard));
        optionsContainer.appendChild(optionCard);
    });
}

// Select an option (implements basic If-Else logic for evaluation)
function selectOption(selectedIndex, selectedCard) {
    if (answerSelected) return; // Prevent clicking multiple times
    
    answerSelected = true;
    const currentQuiz = quizData[currentQuestionIndex];
    const cards = optionsContainer.querySelectorAll(".option-card");
    
    // Control Flow: Check if the user's answer is correct
    if (selectedIndex === currentQuiz.correctIndex) {
        // Correct Answer Logic
        selectedCard.classList.add("correct");
        score = score + 1;
        currentScoreText.innerText = score;
        
        // Success feedback indicator change
        selectedCard.querySelector(".option-indicator").innerHTML = "✓";
    } else {
        // Incorrect Answer Logic
        selectedCard.classList.add("incorrect");
        selectedCard.querySelector(".option-indicator").innerHTML = "✗";
        
        // Highlight correct answer in green
        cards[currentQuiz.correctIndex].classList.add("correct");
        cards[currentQuiz.correctIndex].querySelector(".option-indicator").innerHTML = "✓";
    }
    
    // Style non-selected options
    cards.forEach((card, index) => {
        if (index !== selectedIndex && index !== currentQuiz.correctIndex) {
            card.classList.add("fade-out");
        }
        // Disable all cards
        card.disabled = true;
    });
    
    // Enable "Next" button
    nextBtn.classList.remove("disabled");
    nextBtn.disabled = false;
}

// Handle Next Button Navigation
function handleNextQuestion() {
    if (currentQuestionIndex < quizData.length - 1) {
        currentQuestionIndex++;
        // Fade transition effect
        quizScreen.classList.remove("active");
        setTimeout(() => {
            loadQuestion();
            quizScreen.classList.add("active");
        }, 300);
    } else {
        showResults();
    }
}

// Display final results screen
function showResults() {
    quizScreen.classList.remove("active");
    setTimeout(() => {
        quizScreen.style.display = "none";
        resultsScreen.style.display = "flex";
        setTimeout(() => resultsScreen.classList.add("active"), 50);
        
        // Set up scoreboard display
        scoreFraction.innerText = `${score}/${quizData.length}`;
        
        // Calculate circle progress percentage
        const percentage = (score / quizData.length) * 100;
        circleFill.setAttribute("stroke-dasharray", `${percentage}, 100`);
        
        // Control Flow: Set dynamic feedback depending on score
        if (score === 3) {
            feedbackHeadline.innerText = "🌟 Perfect Score! 🌟";
            feedbackDesc.innerText = "Sensational! You answered all questions perfectly. You're a trivia champion!";
        } else if (score === 2) {
            feedbackHeadline.innerText = "🎉 Well Done! 🎉";
            feedbackDesc.innerText = "Great job! You answered 2 out of 3 questions correctly. Almost perfect!";
        } else if (score === 1) {
            feedbackHeadline.innerText = "👍 Keep Practicing 👍";
            feedbackDesc.innerText = "Not bad! You got 1 correct. Play again to improve your score.";
        } else {
            feedbackHeadline.innerText = "📚 Hit the Books! 📚";
            feedbackDesc.innerText = "You scored 0 out of 3. No worries, trivia is a great way to learn new things!";
        }
    }, 400);
}

// Restart Quiz
function restartQuiz() {
    currentQuestionIndex = 0;
    score = 0;
    
    resultsScreen.classList.remove("active");
    setTimeout(() => {
        resultsScreen.style.display = "none";
        welcomeScreen.style.display = "flex";
        setTimeout(() => welcomeScreen.classList.add("active"), 50);
    }, 400);
}
