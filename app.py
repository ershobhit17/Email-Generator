from flask import Flask, render_template, jsonify, request

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_pitch', methods=['POST'])
def generate_pitch():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400

        name = data.get('name', '').strip()
        skills = data.get('skills', '').strip()
        company = data.get('company', '').strip()
        role = data.get('role', '').strip()
        project = data.get('project', '').strip()

        if not name or not skills or not company or not role:
            return jsonify({"error": "Missing required fields"}), 400

        # --- TONE 1: THE PROFESSIONAL (For MNCs like TCS, Infosys, Big 4) ---
        prof_subject = f"Application for {role} Internship - {name}"
        prof_body = (
            f"Dear Hiring Team at {company},\n\n"
            f"I hope this email finds you well.\n\n"
            f"I am writing to express my strong interest in the {role} Internship opportunity at {company}. "
            f"As a pre-final year engineering student specializing in software development, I have built a solid foundation "
            f"in {skills}. Through rigorous academic learning and hands-on projects, I have developed a keen eye for scalable architecture.\n\n"
            f"A notable demonstration of my technical capabilities is my project: '{project}', where I successfully managed "
            f"end-to-end functionality. Given {company}'s reputation for driving technological innovation, I am eager to contribute my "
            f"technical skills to your ongoing projects while learning from your esteemed engineering team.\n\n"
            f"My resume is attached for your review. I would welcome the opportunity to discuss how my background aligns with your requirements.\n\n"
            f"Thank you for your time and consideration.\n\n"
            f"Sincerely,\n"
            f"{name}\n"
            f"LinkedIn Profile | GitHub Portfolio"
        )

        # --- TONE 2: THE HUNGRY BUILDER (For high-growth startups like Swiggy, Zomato, Razorpay) ---
        builder_subject = f"Building for {company}: Keen to join as a {role} Intern"
        builder_body = (
            f"Hi team {company},\n\n"
            f"I’ve been closely tracking how {company} is scaling engineering systems lately, and it's incredibly fascinating. "
            f"Instead of sending a generic application, I wanted to reach out directly because I love building things that break and scale.\n\n"
            f"I am a developer proficient in {skills}. To put my skills to the test, I built '{project}'. "
            f"I didn't just write the code; I optimized execution time and focused heavily on fixing system bottlenecks.\n\n"
            f"I know startups don't have time to micro-manage interns. I am looking for an opportunity where I can ship code to production on Day 1, "
            f"take ownership, and solve real engineering problems for {company}.\n\n"
            f"My portfolio is attached. Let me know if you have 5 minutes for a quick chat this week.\n\n"
            f"Cheers,\n"
            f"{name}"
        )

        # --- TONE 3: THE HONEST INTERN (Raw, authentic, highly relatable for early-stage startups) ---
        honest_subject = f"{role} Intern position - Quick query from a passionate developer ({name})"
        honest_body = (
            f"Hi,\n\n"
            f"I'll keep this short and straightforward because I know your inbox is constantly flooded.\n\n"
            f"I am an engineering student, and I am desperately looking for an environment where I can put my theoretical knowledge into actual practice. "
            f"I am heavily into coding and have spent the last few months deeply learning {skills}.\n\n"
            f"I recently built a project called '{project}'. It's not perfect, but it taught me how to tackle real development challenges "
            f"and debug code independently when everything falls apart.\n\n"
            f"I am genuinely inspired by what you guys are building at {company}. I don't care about a fancy stipend or perks; "
            f"I just want to sit with smart engineers, learn how production environments work, and contribute to your workload.\n\n"
            f"I have attached my resume. Even if you don't have an opening right now, I'd appreciate any feedback on my profile!\n\n"
            f"Best regards,\n"
            f"{name}"
        )

        return jsonify({
            "success": True,
            "pitches": {
                "professional": {"subject": prof_subject, "body": prof_body},
                "builder": {"subject": builder_subject, "body": builder_body},
                "honest": {"subject": honest_subject, "body": honest_body}
            }
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
