class LessonMap {
    constructor() {
        this.lessonsContainer = document.getElementById('lessons');
        this.initializeMap();
    }

    async initializeMap() {
        await this.fetchLessons();
        this.drawLessons();
    }

    drawLessons() {
        this.lessons.forEach(lesson => {
            const card = document.createElement('div');
            card.className = `lesson-card ${lesson.is_active ? 'active' : 'locked'}`;
            
            // Extract only the English title
            const englishTitle = lesson.title.split('\n')[1];
            
            card.innerHTML = `
                <div class="lesson-header">
                    <div class="lesson-icon">
                        ${this.getLessonIcon(lesson)}
                    </div>
                    <div class="lesson-info">
                        <div class="lesson-number">Lesson ${lesson.id}</div>
                        <div class="lesson-title">${englishTitle}</div>
                    </div>
                </div>
            `;
            
            if (lesson.is_active) {
                card.addEventListener('click', () => this.handleLessonClick(lesson));
            }
            
            this.lessonsContainer.appendChild(card);
        });
    }

    async fetchLessons() {
        const response = await fetch('/api/lessons');
        this.lessons = await response.json();
    }

    handleLessonClick(lesson) {
        if (!lesson.is_active) {
            return;
        }

        // Navigate to lesson page
        window.location.href = `/lesson/${lesson.id}`;
    }

    setupAccessibility() {
        // Add keyboard navigation
        this.container.setAttribute('role', 'application');
        this.container.setAttribute('aria-label', 'Chinese Learning Map');
        
        // Make lessons focusable
        const lessons = this.container.querySelectorAll('.lesson-circle');
        lessons.forEach(lesson => {
            lesson.setAttribute('tabindex', '0');
        });
    }

    unlockConnectedLessons(completedLessonId) {
        this.lessons.forEach(lesson => {
            if (lesson.prerequisites.includes(completedLessonId.toString())) {
                const prerequisites = lesson.prerequisites.split(',').map(Number);
                const allCompleted = prerequisites.every(preReqId => {
                    const preReqLesson = this.lessons.find(l => l.id === preReqId);
                    return preReqLesson && preReqLesson.is_active;
                });
                
                if (allCompleted) {
                    lesson.is_active = true;
                    // Refresh the lesson display
                    this.refreshLessonDisplay(lesson);
                }
            }
        });
    }

    refreshLessonDisplay(lesson) {
        const lessonElement = this.lessonsContainer.querySelector(
            `.lesson-circle[style*="left: ${lesson.position.x}%"][style*="top: ${lesson.position.y}%"]`
        );
        if (lessonElement) {
            lessonElement.className = 'lesson-circle active';
            // Update event listeners
            lessonElement.addEventListener('click', () => this.handleLessonClick(lesson));
        }
    }

    animateNumber(start, end, duration, callback) {
        const startTime = performance.now();
        const change = end - start;

        const animate = (currentTime) => {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function for smooth animation
            const value = start + change * this.easeOutQuad(progress);
            callback(value);

            if (progress < 1) {
                requestAnimationFrame(animate);
            }
        };

        requestAnimationFrame(animate);
    }

    easeOutQuad(t) {
        return t * (2 - t);
    }

    celebrateMilestone(progress) {
        // Create celebratory confetti
        confetti({
            particleCount: 100,
            spread: 70,
            origin: { y: 0.6 },
            colors: ['#ff4d4d', '#ffcd94', '#52c41a']
        });

        // Add milestone message
        const messages = {
            25: "Great start! You're getting the hang of it! 加油！",
            50: "Halfway there! You're doing amazing! 非常好！",
            75: "Almost there! You're becoming a master! 太棒了！",
            100: "Incredible achievement! You're a Chinese learning star! 恭喜！"
        };

        if (messages[progress]) {
            const tooltip = document.createElement('div');
            tooltip.className = 'milestone-tooltip';
            tooltip.textContent = messages[progress];
            document.body.appendChild(tooltip);

            setTimeout(() => {
                tooltip.remove();
            }, 3000);
        }
    }

    getLessonIcon(lesson) {
        // Add icons based on lesson status
        if (!lesson.is_active) {
            return '🔒';
        }
        // You can customize icons based on lesson type/content
        return '📖';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new LessonMap();
}); 