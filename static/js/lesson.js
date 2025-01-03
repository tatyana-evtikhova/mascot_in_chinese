class NotionLikeLesson {
    constructor() {
        this.initializeCollapsibles();
        this.initializeTableOfContents();
        this.initializeProgressTracking();
        this.setupChineseCharacters();
        this.initializeTTS();
        this.setupChineseTextInteraction();
        this.setupWordCards();
    }

    initializeCollapsibles() {
        document.querySelectorAll('.collapsible-header').forEach(header => {
            header.addEventListener('click', () => {
                const content = header.nextElementSibling;
                const isOpen = content.style.maxHeight;

                if (isOpen) {
                    content.style.maxHeight = null;
                    header.classList.remove('open');
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                    header.classList.add('open');
                }
            });
        });
    }

    initializeTableOfContents() {
        const toc = document.querySelector('.toc');
        const sections = document.querySelectorAll('.section-header');
        
        // Create TOC items
        sections.forEach(section => {
            const link = document.createElement('a');
            link.href = `#${section.id}`;
            link.className = 'toc-item';
            link.textContent = section.querySelector('.section-title').textContent;
            toc.appendChild(link);
        });

        // Highlight active section
        window.addEventListener('scroll', () => {
            let currentSection = '';
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (window.pageYOffset >= sectionTop - 100) {
                    currentSection = section.id;
                }
            });

            document.querySelectorAll('.toc-item').forEach(item => {
                item.classList.toggle('active', item.getAttribute('href') === `#${currentSection}`);
            });
        });
    }

    initializeProgressTracking() {
        const progressFill = document.querySelector('.progress-fill');
        
        window.addEventListener('scroll', () => {
            const windowHeight = window.innerHeight;
            const fullHeight = document.documentElement.scrollHeight - windowHeight;
            const scrolled = window.pageYOffset;
            const progress = (scrolled / fullHeight) * 100;
            
            progressFill.style.width = `${progress}%`;
        });
    }

    setupChineseCharacters() {
        document.querySelectorAll('.chinese-character').forEach(char => {
            char.addEventListener('click', () => {
                // Play audio if available
                const audio = char.dataset.audio;
                if (audio) {
                    new Audio(audio).play();
                }

                // Visual feedback
                char.classList.add('playing');
                setTimeout(() => char.classList.remove('playing'), 500);
            });
        });
    }

    initializeTTS() {
        this.synth = window.speechSynthesis;
        // Get Chinese voice if available
        this.voices = [];
        
        speechSynthesis.addEventListener('voiceschanged', () => {
            this.voices = this.synth.getVoices();
            this.chineseVoice = this.voices.find(voice => 
                voice.lang.includes('zh') || voice.lang.includes('cmn')
            );
        });
    }

    setupChineseTextInteraction() {
        document.querySelectorAll('.chinese-text').forEach(element => {
            element.addEventListener('click', () => this.speakText(element.textContent));
            
            // Add hover effect
            element.addEventListener('mouseenter', () => {
                element.style.backgroundColor = 'var(--notion-hover-bg)';
            });
            
            element.addEventListener('mouseleave', () => {
                element.style.backgroundColor = 'transparent';
            });
        });
    }

    speakText(text) {
        if (this.synth.speaking) {
            this.synth.cancel();
        }

        const utterance = new SpeechSynthesisUtterance(text);
        utterance.voice = this.chineseVoice;
        utterance.rate = 0.9;
        utterance.pitch = 1;
        
        // Add subtle visual feedback
        const element = document.querySelector(`.chinese-text:contains("${text}")`);
        if (element) {
            element.style.backgroundColor = 'var(--notion-hover-bg)';
            setTimeout(() => {
                element.style.backgroundColor = 'transparent';
            }, 200);
        }

        this.synth.speak(utterance);
    }

    setupWordCards() {
        document.querySelectorAll('.word-card').forEach(card => {
            card.addEventListener('click', () => {
                const chinese = card.querySelector('.word-chinese').textContent;
                this.speakText(chinese);
                
                // Add visual feedback
                card.style.backgroundColor = 'var(--notion-hover-bg)';
                setTimeout(() => {
                    card.style.backgroundColor = 'white';
                }, 200);
            });
        });
    }
}

// Initialize when the DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new NotionLikeLesson();
}); 