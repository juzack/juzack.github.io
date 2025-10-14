// Brittany Chiang 스타일 포트폴리오 JavaScript

// DOM이 로드된 후 실행
document.addEventListener('DOMContentLoaded', function() {
    // 네비게이션 기능 초기화
    initNavigation();
    
    // 탭 기능 초기화
    initTabs();
    
    // 스크롤 애니메이션 초기화
    initScrollAnimations();
    
    // 부드러운 스크롤 초기화
    initSmoothScroll();
    
    // 타이핑 효과 초기화
    initTypingEffect();
    
    // 프로젝트 호버 효과 초기화
    initProjectHover();
    
    // 스크롤 진행률 표시
    initScrollProgress();
    
    // 키보드 네비게이션
    initKeyboardNavigation();
});

// 네비게이션 기능 초기화
function initNavigation() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.section');
    
    // 현재 섹션에 따른 네비게이션 활성화
    function updateActiveNavLink() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (window.scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('active');
            }
        });
    }

    // 스크롤 이벤트 최적화
    let ticking = false;
    function updateOnScroll() {
        if (!ticking) {
            requestAnimationFrame(() => {
                updateActiveNavLink();
                ticking = false;
            });
            ticking = true;
        }
    }

    window.addEventListener('scroll', updateOnScroll);
    
    // 초기 활성화
    updateActiveNavLink();
}

// 탭 기능 초기화
function initTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabPanels = document.querySelectorAll('.tab-panel');
    
    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const targetTab = button.getAttribute('data-tab');
            
            // 모든 탭 버튼과 패널 비활성화
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabPanels.forEach(panel => panel.classList.remove('active'));
            
            // 선택된 탭 활성화
            button.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// 스크롤 애니메이션 초기화
function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                
                // 특별한 애니메이션 효과들
                if (entry.target.classList.contains('project-item')) {
                    setTimeout(() => {
                        entry.target.style.transform = 'translateY(0)';
                    }, 100);
                }
            }
        });
    }, observerOptions);

    // 애니메이션할 요소들 선택
    const animateElements = document.querySelectorAll(
        '.about-text, .skills-section, .tab-panel, .project-item, .contact-text'
    );
    
    animateElements.forEach(el => {
        el.classList.add('scroll-animate');
        observer.observe(el);
    });
}

// 부드러운 스크롤 초기화
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const offsetTop = targetSection.offsetTop;
                
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// 타이핑 효과 초기화
function initTypingEffect() {
    const greeting = document.querySelector('.greeting');
    const name = document.querySelector('.name');
    const title = document.querySelector('.title');
    
    if (!greeting || !name || !title) return;
    
    // 초기 상태 설정
    greeting.style.opacity = '0';
    name.style.opacity = '0';
    title.style.opacity = '0';
    
    // 순차적으로 나타나는 효과
    setTimeout(() => {
        greeting.style.transition = 'opacity 0.6s ease';
        greeting.style.opacity = '1';
    }, 500);
    
    setTimeout(() => {
        name.style.transition = 'opacity 0.6s ease';
        name.style.opacity = '1';
    }, 1000);
    
    setTimeout(() => {
        title.style.transition = 'opacity 0.6s ease';
        title.style.opacity = '1';
    }, 1500);
}

// 프로젝트 호버 효과 초기화
function initProjectHover() {
    const projectItems = document.querySelectorAll('.project-item');
    
    projectItems.forEach(item => {
        item.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.borderColor = 'var(--green)';
        });
        
        item.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.borderColor = 'transparent';
        });
    });
}

// 스크롤 진행률 표시
function initScrollProgress() {
    const progressBar = document.createElement('div');
    progressBar.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 0%;
        height: 2px;
        background: linear-gradient(90deg, var(--green), var(--blue));
        z-index: 9999;
        transition: width 0.1s ease;
    `;
    document.body.appendChild(progressBar);

    function updateProgress() {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        progressBar.style.width = scrolled + '%';
    }

    window.addEventListener('scroll', updateProgress);
}

// 키보드 네비게이션
function initKeyboardNavigation() {
    document.addEventListener('keydown', function(e) {
        // Tab 키로 네비게이션 링크 포커스
        if (e.key === 'Tab') {
            const activeElement = document.activeElement;
            if (activeElement.classList.contains('nav-link')) {
                activeElement.style.outline = '2px solid var(--green)';
            }
        }
        
        // Escape 키로 포커스 해제
        if (e.key === 'Escape') {
            document.activeElement.blur();
        }
        
        // 화살표 키로 탭 네비게이션
        if (e.key === 'ArrowLeft' || e.key === 'ArrowRight') {
            const activeTab = document.querySelector('.tab-button.active');
            if (activeTab) {
                e.preventDefault();
                const tabs = Array.from(document.querySelectorAll('.tab-button'));
                const currentIndex = tabs.indexOf(activeTab);
                let nextIndex;
                
                if (e.key === 'ArrowLeft') {
                    nextIndex = currentIndex > 0 ? currentIndex - 1 : tabs.length - 1;
                } else {
                    nextIndex = currentIndex < tabs.length - 1 ? currentIndex + 1 : 0;
                }
                
                tabs[nextIndex].click();
                tabs[nextIndex].focus();
            }
        }
    });
}

// 페이지 로드 완료 후 추가 애니메이션
window.addEventListener('load', function() {
    // 히어로 섹션 요소들에 페이드인 효과
    const heroElements = document.querySelectorAll('.hero > *');
    heroElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            el.style.transition = 'all 0.8s ease';
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, 200 + (index * 200));
    });
    
    // 사이드바 소셜 링크 애니메이션
    const socialLinks = document.querySelectorAll('.social-links a');
    socialLinks.forEach((link, index) => {
        link.style.opacity = '0';
        link.style.transform = 'translateY(20px)';
        
        setTimeout(() => {
            link.style.transition = 'all 0.5s ease';
            link.style.opacity = '1';
            link.style.transform = 'translateY(0)';
        }, 1000 + (index * 100));
    });
});

// 반응형 네비게이션 (모바일용)
function handleResize() {
    const sidebar = document.querySelector('.sidebar');
    const mainContent = document.querySelector('.main-content');
    
    if (window.innerWidth <= 768) {
        sidebar.style.display = 'none';
        mainContent.style.marginLeft = '0';
    } else {
        sidebar.style.display = 'flex';
        mainContent.style.marginLeft = '100px';
    }
}

window.addEventListener('resize', handleResize);

// 성능 최적화를 위한 디바운스 함수
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// 스크롤 이벤트 최적화
const optimizedScrollHandler = debounce(function() {
    // 스크롤 관련 기능들
}, 10);

window.addEventListener('scroll', optimizedScrollHandler);

// 마우스 커서 효과 (선택사항)
function initCustomCursor() {
    const cursor = document.createElement('div');
    cursor.className = 'custom-cursor';
    cursor.style.cssText = `
        position: fixed;
        width: 20px;
        height: 20px;
        background: var(--green);
        border-radius: 50%;
        pointer-events: none;
        z-index: 9999;
        opacity: 0.5;
        transition: transform 0.1s ease;
        display: none;
    `;
    document.body.appendChild(cursor);

    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX - 10 + 'px';
        cursor.style.top = e.clientY - 10 + 'px';
        cursor.style.display = 'block';
    });

    document.addEventListener('mouseleave', () => {
        cursor.style.display = 'none';
    });

    // 호버 효과
    const hoverElements = document.querySelectorAll('a, button, .project-item');
    hoverElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.style.transform = 'scale(1.5)';
        });
        el.addEventListener('mouseleave', () => {
            cursor.style.transform = 'scale(1)';
        });
    });
}

// 커스텀 커서 초기화 (데스크톱에서만)
if (window.innerWidth > 768) {
    initCustomCursor();
}

// 접근성 개선
function initAccessibility() {
    // 스킵 링크 추가
    const skipLink = document.createElement('a');
    skipLink.href = '#main';
    skipLink.textContent = '메인 콘텐츠로 건너뛰기';
    skipLink.className = 'skip-link';
    skipLink.style.cssText = `
        position: absolute;
        top: -40px;
        left: 6px;
        background: var(--green);
        color: var(--dark-navy);
        padding: 8px;
        text-decoration: none;
        border-radius: 4px;
        z-index: 10000;
        transition: top 0.3s;
    `;
    
    skipLink.addEventListener('focus', () => {
        skipLink.style.top = '6px';
    });
    
    skipLink.addEventListener('blur', () => {
        skipLink.style.top = '-40px';
    });
    
    document.body.insertBefore(skipLink, document.body.firstChild);
    
    // 메인 콘텐츠에 ID 추가
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.id = 'main';
    }
}

// 접근성 초기화
initAccessibility();

// 에러 핸들링
window.addEventListener('error', function(e) {
    console.error('JavaScript Error:', e.error);
});

// 페이지 가시성 변경 감지
document.addEventListener('visibilitychange', function() {
    if (document.hidden) {
        // 페이지가 숨겨졌을 때 애니메이션 일시정지
        document.body.style.animationPlayState = 'paused';
    } else {
        // 페이지가 다시 보일 때 애니메이션 재개
        document.body.style.animationPlayState = 'running';
    }
});

// 로딩 완료 후 초기화
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function() {
        console.log('Portfolio loaded successfully!');
    });
} else {
    console.log('Portfolio loaded successfully!');
}