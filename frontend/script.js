function toggleProfileMenu() {
    const menu = document.getElementById("profile-menu");
    menu.style.display = menu.style.display === "block" ? "none" : "block";
}

function showUserJourney() {
    const probability = calculateCourseProbability();
    alert(`Probability of user taking the course: ${probability}%`);
}

function showNewLearning() {
    alert("Showing new learning...");
}

function showCertifications() {
    alert("Showing certifications...");
}

function calculateCourseProbability() {
    const userPerformance = Math.random() * 100; // Simulated user performance
    const topicInterest = Math.random() * 100; // Simulated interest in the topic
    return Math.round((userPerformance + topicInterest) / 2); // Simple average for probability
}

function loadProgressChart() {
    const ctx = document.getElementById('progressChart').getContext('2d');
    const randomData = Array.from({ length: 5 }, () => Math.floor(Math.random() * 100)); // Random data

    const chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5'],
            datasets: [{
                label: 'Progress',
                data: randomData,
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderWidth: 1,
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            }
        }
    });
}

function loadRecommendedCourses() {
    const courses = [
        { title: "Introduction to Python", description: "Learn the basics of Python programming." },
        { title: "Advanced JavaScript", description: "Deep dive into JavaScript programming." },
        { title: "Data Science Essentials", description: "Understand the key concepts of Data Science." },
    ];

    const coursesContainer = document.getElementById('courses');
    courses.forEach(course => {
        const card = document.createElement('div');
        card.className = 'course-card';
        card.innerHTML = `<strong>${course.title}</strong><p>${course.description}</p>`;
        coursesContainer.appendChild(card);
    });
}

function toggleChatbot() {
    const popup = document.getElementById("chatbot-popup");
    popup.style.display = popup.style.display === "block" ? "none" : "block";
}

function sendMessage() {
    const message = document.getElementById("chat-input").value;
    alert(`You asked: "${message}"`); // Placeholder for handling the message
    document.getElementById("chat-input").value = ''; // Clear input
}

window.onload = function() {
    loadProgressChart();
    loadRecommendedCourses();
};
