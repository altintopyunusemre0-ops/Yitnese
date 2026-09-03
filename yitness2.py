# ==============================================================================
# WEB SİTESİ ADI: yitness
# GELİŞTİRİCİ / TASARIMCI: yunus emre altintop
# DİL / FRAMEWORK: Python (Flask) & HTML/CSS/JavaScript
# KULLANIM ALANI: VS Code uyumlu tek dosya web uygulaması
# ==============================================================================

from flask import Flask, render_template_string

app = Flask(__name__)

# ------------------------------------------------------------------------------
# HTML, CSS VE JAVASCRIPT ARAYÜZ TASARIMI
# ------------------------------------------------------------------------------
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>yitness</title>
    <style>
        /* Genel Tema: Beyaz Arka Plan, Koyu Gri Yazı Renkleri */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: #ffffff;
            color: #333333;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            position: relative;
        }

        /* Header Başlık */
        header {
            margin-top: 15px;
            margin-bottom: 30px;
            text-align: center;
        }

        h1.site-title {
            font-size: 3rem;
            letter-spacing: -1px;
            color: #222222;
            font-weight: 700;
            text-transform: lowercase;
        }

        p.subtitle {
            color: #666666;
            font-size: 0.95rem;
            margin-top: 5px;
        }

        /* Ana Panel Konfigürasyonu */
        .dashboard {
            width: 100%;
            max-width: 950px;
            display: grid;
            grid-template-columns: 1fr 1.2fr;
            gap: 30px;
            align-items: start;
            margin-bottom: 80px;
        }

        @media (max-width: 768px) {
            .dashboard {
                grid-template-columns: 1fr;
            }
        }

        /* İnsan Anatomisi Görsel Alanı */
        .anatomy-section {
            background: #fafafa;
            border: 1px solid #e5e5e5;
            border-radius: 12px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .anatomy-title {
            font-size: 1rem;
            color: #444444;
            margin-bottom: 15px;
            font-weight: 600;
        }

        /* Gri İnsan Anatomisi Silüeti */
        .anatomy-svg {
            width: 100%;
            max-width: 260px;
            height: auto;
        }

        .body-part {
            fill: #9e9e9e; /* Gri İnsan Rengi */
            stroke: #ffffff;
            stroke-width: 1.5;
            cursor: pointer;
            transition: fill 0.2s ease;
        }

        .body-part:hover, .body-part.selected {
            fill: #e63946; /* Tıklanan Bölge Kırmızı Olur */
        }

        .anatomy-legend {
            display: flex;
            gap: 8px;
            margin-top: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }

        .legend-tag {
            background-color: #eeeeee;
            color: #4a4a4a;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            cursor: pointer;
            border: 1px solid #ddd;
            transition: all 0.2s;
        }

        .legend-tag:hover, .legend-tag.active {
            background-color: #e63946;
            color: #ffffff;
            border-color: #e63946;
        }

        /* Egzersiz Bilgi Alanı */
        .workout-section {
            background: #ffffff;
            border: 1px solid #e0e0e0;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.02);
        }

        .workout-header {
            font-size: 1.3rem;
            color: #222222;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 2px solid #f0f0f0;
        }

        .exercise-card {
            background: #fdfdfd;
            border-left: 4px solid #e63946;
            border-top: 1px solid #f0f0f0;
            border-right: 1px solid #f0f0f0;
            border-bottom: 1px solid #f0f0f0;
            padding: 14px;
            margin-bottom: 12px;
            border-radius: 0 8px 8px 0;
        }

        .exercise-name {
            font-size: 1rem;
            font-weight: 600;
            color: #333333;
            margin-bottom: 4px;
        }

        .exercise-details {
            font-size: 0.88rem;
            color: #666666;
            line-height: 1.4;
        }

        .badge-home {
            display: inline-block;
            background-color: #e8f5e9;
            color: #2e7d32;
            font-size: 0.75rem;
            padding: 2px 8px;
            border-radius: 4px;
            margin-top: 6px;
            font-weight: 500;
        }

        /* Sağ Alt Köşe İmzası */
        .footer-credit {
            position: fixed;
            bottom: 12px;
            right: 18px;
            font-style: italic; /* İtalik */
            font-weight: 300;  /* İnce */
            color: #777777;    /* Gri */
            font-size: 0.88rem;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.9);
            padding: 4px 8px;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <!-- Başlık -->
    <header>
        <h1 class="site-title">yitness</h1>
        <p class="subtitle">Home Workout Guide</p>
    </header>

    <!-- Ana Panel: Maket ve Bilgi Ekranı -->
    <div class="dashboard">
        
        <!-- İnsan Anatomisi Maketi -->
        <div class="anatomy-section">
            <div class="anatomy-title">Select Body Region</div>
            
            <svg class="anatomy-svg" viewBox="0 0 200 400" xmlns="http://www.w3.org/2000/svg">
                <!-- Baş -->
                <circle cx="100" cy="35" r="20" fill="#757575" />
                <!-- Boyun -->
                <rect x="94" y="55" width="12" height="12" fill="#757575" />
                
                <!-- Omuz Bölgesi (Shoulders) -->
                <path id="shoulders" class="body-part" d="M 60,70 Q 100,60 140,70 L 155,90 L 140,95 L 130,80 L 70,80 L 60,95 L 45,90 Z" onclick="showWorkout('shoulders')">
                    <title>Shoulders (Omuz)</title>
                </path>
                
                <!-- Kol Bölgesi (Arms) -->
                <path id="arms-left" class="body-part" d="M 45,90 L 60,95 L 52,160 L 38,155 Z" onclick="showWorkout('arms')">
                    <title>Left Arm (Kol)</title>
                </path>
                <path id="arms-right" class="body-part" d="M 155,90 L 140,95 L 148,160 L 162,155 Z" onclick="showWorkout('arms')">
                    <title>Right Arm (Kol)</title>
                </path>

                <!-- Karın Bölgesi (Abs & Core) -->
                <path id="abs" class="body-part" d="M 70,80 L 130,80 L 125,170 L 75,170 Z" onclick="showWorkout('abs')">
                    <title>Abs & Core (Karın)</title>
                </path>

                <!-- Kalça / Bel -->
                <polygon points="75,170 125,170 130,200 70,200" fill="#757575" />

                <!-- Bacak Bölgesi (Legs) -->
                <path id="legs-left" class="body-part" d="M 70,200 L 97,200 L 94,360 L 72,360 Z" onclick="showWorkout('legs')">
                    <title>Left Leg (Bacak)</title>
                </path>
                <path id="legs-right" class="body-part" d="M 103,200 L 130,200 L 128,360 L 106,360 Z" onclick="showWorkout('legs')">
                    <title>Right Leg (Bacak)</title>
                </path>
            </svg>

            <!-- Hızlı Tıklama Etiketleri -->
            <div class="anatomy-legend">
                <span id="tag-shoulders" class="legend-tag" onclick="showWorkout('shoulders')">Shoulders</span>
                <span id="tag-arms" class="legend-tag" onclick="showWorkout('arms')">Arms</span>
                <span id="tag-abs" class="legend-tag" onclick="showWorkout('abs')">Abs</span>
                <span id="tag-legs" class="legend-tag" onclick="showWorkout('legs')">Legs</span>
            </div>
        </div>

        <!-- Evde Yapılacak Egzersiz Bilgileri -->
        <div class="workout-section">
            <div class="workout-header">
                <span id="target-title">Home Exercises</span>
            </div>
            <div id="exercise-list">
                <!-- Seçilen bölgenin egzersizleri buraya yüklenecek -->
            </div>
        </div>

    </div>

    <!-- Sağ Alt Köşe İmzası -->
    <div class="footer-credit">
        yunus emre altintop
    </div>

    <!-- EVDE YAPILACAK EGZERSİZ BİLGİLERİ -->
    <script>
        const workoutData = {
            shoulders: [
                { name: "Pike Push-Up", reps: "3 Sets x 10-12 Reps", desc: "Elevate your hips into an inverted V-position to target the anterior and side deltoids." },
                { name: "Wall Walk", reps: "3 Sets x 5 Reps", desc: "Start in a push-up position and walk your feet up the wall into a handstand position." },
                { name: "Elevated Pike Push-Up", reps: "3 Sets x 8-10 Reps", desc: "Place feet on a chair or couch to increase resistance on shoulder muscles." },
                { name: "Reverse Snow Angels", reps: "3 Sets x 15 Reps", desc: "Lie face down and move arms in a controlled arc to engage rear delts and upper back." },
                { name: "Y-T-W Raises", reps: "3 Sets x 12 Reps", desc: "Form Y, T, and W shapes with your arms while lying prone to build shoulder stability." }
            ],
            legs: [
                { name: "Sumo Squat", reps: "4 Sets x 15 Reps", desc: "Wide stance with toes pointed outward to target inner thighs and glutes." },
                { name: "Bulgarian Split Squat", reps: "3 Sets x 12 Reps / leg", desc: "Rest one foot behind on a chair/bed to isolate quads and glutes intensely." },
                { name: "Lunges", reps: "3 Sets x 12 Reps / leg", desc: "Step forward alternating legs to build quad strength and improve balance." },
                { name: "Single-Leg Glute Bridge", reps: "3 Sets x 15 Reps / leg", desc: "Lie back, extend one leg, and lift hips up to target hamstrings and glutes." },
                { name: "Wall Sit", reps: "3 Sets x 45-60 Seconds", desc: "Press back flat against a wall with knees at a 90-degree angle for static quad burn." },
                { name: "Calf Raises", reps: "4 Sets x 20 Reps", desc: "Raise up onto the balls of your feet to strengthen calf muscles." }
            ],
            abs: [
                { name: "Crunches", reps: "3 Sets x 20 Reps", desc: "Lie flat with knees bent and lift upper back off the floor to isolate upper abdominals." },
                { name: "Leg Raises", reps: "3 Sets x 15 Reps", desc: "Lie on your back and raise straight legs vertically to target lower abs." },
                { name: "Plank", reps: "3 Sets x 60 Seconds", desc: "Hold body in a straight line on forearms and toes to build core stability." },
                { name: "Mountain Climbers", reps: "3 Sets x 30 Seconds", desc: "Drive knees toward chest rapidly from a push-up position for core and cardio." },
                { name: "Russian Twists", reps: "3 Sets x 20 Reps", desc: "Sit up slightly, balance on glutes, and twist torso side to side for obliques." },
                { name: "Bicycle Crunches", reps: "3 Sets x 20 Reps", desc: "Alternate elbow to opposite knee to engage entire abdominal wall and obliques." },
                { name: "Hollow Body Hold", reps: "3 Sets x 30-45 Seconds", desc: "Press lower back to floor while keeping arms and legs elevated off the ground." }
            ],
            arms: [
                { name: "Diamond Push-Up", reps: "3 Sets x 12 Reps", desc: "Form a diamond shape with hands under chest to heavily target triceps." },
                { name: "Chair Dips", reps: "3 Sets x 15 Reps", desc: "Place hands on sturdy chair edge behind you to lower and raise body for triceps." },
                { name: "Bodyweight Biceps Curl", reps: "3 Sets x 12 Reps", desc: "Use a doorframe or towel wrapped around a post to pull body weight upward." },
                { name: "Table Row", reps: "3 Sets x 10 Reps", desc: "Lie under a sturdy table, grip the edge, and pull chest up to train back and biceps." },
                { name: "Plank Shoulder Taps", reps: "3 Sets x 20 Taps", desc: "Hold high plank position while tapping opposite shoulder to build arm and core stability." },
                { name: "Chin-Up Hold", reps: "3 Sets x 15-20 Seconds", desc: "Grip a doorframe, sturdy bar, or ledge to hold body weight isometric position." },
                { name: "Forearm Plank to Push-Up", reps: "3 Sets x 10 Reps", desc: "Transition between forearm plank and high push-up position to work arms and shoulders." }
            ]
        };

        function showWorkout(group) {
            // Görsel seçim efektleri
            document.querySelectorAll('.body-part').forEach(el => el.classList.remove('selected'));
            document.querySelectorAll('.legend-tag').forEach(el => el.classList.remove('active'));

            if(group === 'arms') {
                document.getElementById('arms-left').classList.add('selected');
                document.getElementById('arms-right').classList.add('selected');
                document.getElementById('tag-arms').classList.add('active');
            } else if(group === 'legs') {
                document.getElementById('legs-left').classList.add('selected');
                document.getElementById('legs-right').classList.add('selected');
                document.getElementById('tag-legs').classList.add('active');
            } else if(document.getElementById(group)) {
                document.getElementById(group).classList.add('selected');
                document.getElementById('tag-' + group).classList.add('active');
            }

            const titleMap = {
                arms: "Arm Exercises (Home)",
                legs: "Leg Exercises (Home)",
                shoulders: "Shoulder Exercises (Home)",
                abs: "Abs & Core Exercises (Home)"
            };

            document.getElementById('target-title').innerText = titleMap[group];
            
            const listContainer = document.getElementById('exercise-list');
            listContainer.innerHTML = '';

            workoutData[group].forEach(ex => {
                const card = document.createElement('div');
                card.className = 'exercise-card';
                card.innerHTML = `
                    <div class="exercise-name">${ex.name}</div>
                    <div class="exercise-details">${ex.desc}</div>
                    <div style="margin-top: 6px; font-weight: 600; color: #e63946; font-size: 0.85rem;">${ex.reps}</div>
                    <span class="badge-home">100% Home Exercise</span>
                `;
                listContainer.appendChild(card);
            });
        }

        // Sayfa açıldığında doğrudan Kol hareketleri ile başlar
        window.onload = function() {
            showWorkout('arms');
        };
    </script>
</body>
</html>
"""

# # (ad "Flask Web Rota Tanımlaması")
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# # (ad "Çalıştırma Ayarları")
if __name__ == '__main__':
    app.run(debug=True, port=5000)
    if __name__ == '__main__':
        app.run(debug=True)
    