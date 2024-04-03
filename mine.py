from flask import Flask, render_template, request, redirect, url_for, session, flash, render_template_string
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, validators
from wtforms.validators import DataRequired, Email, ValidationError
from flask_bcrypt import Bcrypt
import email_validator
from datetime import timedelta
from datetime import datetime, date
import random
import re
import secrets


from flask_mail import Mail, Message
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__, static_url_path='/static')
app.secret_key = 'makapasasafinals'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = 'mental_thrive'

app.config['MAIL_SERVER'] = 'localhost'
app.config['MAIL_PORT'] = 'root'
app.config['MAIL_USERNAME'] = ""
app.config['MAIL_PASSWORD'] = 'mental_thrive'
app.config['MAIL_USE_TL'] = 'mental_thrive'

mysql = MySQL(app)
bcrypt = Bcrypt(app)


# Our Home page
@app.route('/')
def Mhome():
    return render_template('start_page.html')


#                           "STATION OF COUNSELOR BUTTON"

class CounselorRegistrationForm(FlaskForm):
    Cemail = StringField("", validators=[DataRequired(), Email()])
    Cpassword = PasswordField("", validators=[DataRequired()])
    Signup = SubmitField("Sign up now")


class CounselorLoginForm(FlaskForm):
    Cemail = StringField(
        "", validators=[DataRequired(), Email(message="Email not Registered")])
    Cpassword = PasswordField("", validators=[DataRequired()])
    Login = SubmitField("Login")


# When the user clicks the sign up, it will directly go to counsel registration page
# Rendering the counselor registration page
# Counselor registration

@app.route('/counsel_register', methods=['GET', 'POST'])
def goto_counselor_register():
    form = CounselorRegistrationForm()
    if form.validate_on_submit():
        Cemail = form.Cemail.data
        Cpassword = form.Cpassword.data
        pattern = r"^[a-zA-Z0-9._%+-]+.ui@phinmaed.com$"
        hashed_password = bcrypt.generate_password_hash(
            Cpassword.encode('utf-8').decode('utf-8'))

    # store data in our database
        if re.match(pattern, Cemail):
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT * FROM mental_thrive.counselor_portal WHERE Cemail = %s", (Cemail, ))
            counselor_check = cursor.fetchone()

            if counselor_check:
                flash("This email is already taken.")
                return redirect(url_for('goto_counselor_register'))
            else:
                cursor.execute(
                    " INSERT INTO mental_thrive.counselor_portal (Cemail, Cpassword, status) VALUES (%s, %s, %s)", (Cemail, hashed_password, False))
                mysql.connection.commit()
                cursor.close()
                flash(
                    "Your registration is pending approval from admin. Please be back after 5 minutes and try to login.")
                return redirect(url_for('goto_counselor_login'))
        else:
            flash("Invalid email!")

    return render_template('counsel_register.html', form=form)


# When the user clicks the COUNSELOR button, it will directly go to counsel login page.
# Rendering the counselor login page
# Counselor login

@app.route('/counsel_login', methods=['GET', 'POST'])
def goto_counselor_login():
    form = CounselorLoginForm()
    if form.validate_on_submit():
        Cemail = form.Cemail.data
        Cpassword = form.Cpassword.data

        # Retrieve the hashed password and status from the database
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT Cpassword, status FROM mental_thrive.counselor_portal WHERE Cemail=%s", (Cemail,))
        counselor_result = cursor.fetchone()
        cursor.close()

        if counselor_result:
            hashed_password = counselor_result[0]
            status = counselor_result[1]
            if bcrypt.check_password_hash(hashed_password, Cpassword.encode('utf-8').decode('utf-8')):
                if status == 1:
                    cursor = mysql.connection.cursor()
                    cursor.execute(
                        "SELECT counselor_id FROM mental_thrive.counselor_portal WHERE Cemail=%s", (Cemail,))
                    counselor_id = cursor.fetchone()[0]
                    cursor.close()
                    session['counselor_id'] = counselor_id
                    return redirect(url_for('goto_counselor_landingpage'))
                else:
                    flash("Your account is still pending, when a few minutes pass without confirmation, it means you have not been recognized as a counselor.")
                    return redirect(url_for('goto_counselor_login'))
            else:
                flash("Invalid Credentials! Please try again.")
                return redirect(url_for('goto_counselor_login'))
        else:
            flash("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_counselor_login'))

    return render_template('counsel_login.html', form=form)


password_reset_tokens = {}


@app.route('/forgot_password_counselor', methods=['GET', 'POST'])
def goto_forgot_password_counselor():
    if request.method == 'POST':
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT Cemail, Cpassword FROM counselor_portal WHERE Cemail = %s", (email,))
        user_reset = cursor.fetchone()

        if user_reset:
            token = secrets.token_urlsafe(16)  # Generate a secure random token

            # Store the token in the database
            cursor.execute(
                "UPDATE counselor_portal SET reset_token = %s WHERE Cemail = %s", (token, email))
            mysql.connection.commit()

            # Send email with password reset link
            send_reset_password_email(email, token)

            print(
                'An email with instructions to reset your password has been sent to your email address.')
            return redirect(url_for('goto_counselor_login'))
        else:
            print('Email address not found. Please try again.')

    return render_template('forgot_password_counselor.html')


def send_reset_password_email(email, token):
    sender_email = 'kypa.pama.ui@phinmaed.com'  # Sender's email address
    receiver_email = email
    subject = 'Mental Thrive Password Reset'
    body = f"Reset Your Password\nCounselor\nClick the following link to reset your password: {
        url_for('goto_reset_password_counselor', token=token, _external=True)}"

    # Create message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'lbpf kjng bngw uvco')
        server.sendmail(sender_email, receiver_email, message.as_string())


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def goto_reset_password_counselor(token):
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            # Fetch email from the database based on the token
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT Cemail FROM counselor_portal WHERE reset_token = %s", (token,))
            ang_email = cursor.fetchone()
            cursor.close()

            if ang_email:
                hashed_password = bcrypt.generate_password_hash(
                    new_password).decode('utf-8')
                # Update password in the database
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "UPDATE counselor_portal SET Cpassword = %s WHERE Cemail = %s", (hashed_password, ang_email[0]))
                mysql.connection.commit()
                cursor.close()

                # Redirect to login page after password reset
                return redirect(url_for('goto_counselor_login'))
            else:
                print(
                    'Invalid or expired token. Please request a new password reset link.')
        else:
            print('Passwords do not match. Please try again.')

    # If password reset fails, render the reset password page again
    return render_template('reset_password_counselor.html', token=token)


@app.route('/counsel_logout')
def goto_counselor_logout():
    session.pop('counselor_id', None)
    return redirect(url_for('goto_counselor_login'))


# It will go to counselor landing page
@app.route('/counselor_landingpage')
def goto_counselor_landingpage():
    if 'counselor_id' not in session:
        return redirect(url_for('goto_counselor_login'))
    print(session)

    titletips = ["Set Clear Goals:", "Break Tasks into Manageable Steps:",
                 "Celebrate Progress:", "Surround Yourself with Positivity:", "Practice Self-Care:"]
    rantips = random.choice(titletips)
    indxtips = titletips.index(rantips)
    tips = ["Define specific, measurable, achievable, relevant, and time-bound goals. Having a clear sense of purpose and direction can provide motivation and focus.",
            "Large tasks can be overwhelming. Achieving these smaller goals provides a sense of accomplishment and motivates you to tackle the next one.",
            "Acknowledge and celebrate your achievements, no matter how small. Recognize your progress, a positive mindset and encourages continued effort.",
            "Surround yourself with positivy, whether it's supportive friends and family. Positive environments can contribute to a more optimistic outlook.",
            "Take care of your physical and mental well-being. Ensure you get enough rest, eat nutritious meals, and make time for activities you enjoy."]

    resulttitle = rantips
    result = tips[indxtips]

    return render_template('counselor_landingpage.html', resulttitle=resulttitle, result=result)


# When the user clicks the home button, it will directly go to home page.
@app.route('/start_page')
def all_buttons_backhome():
    return render_template('start_page.html')

# It will go to counselor dashboard


@app.route('/counselor_dash')
def goto_counselor_dash():

    # Fetch updated student records #ging butong ya ang email kag name sa student portal
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT student_portal.Semail, student_portal.Sfirst_name, student_portal.Slast_name, student_portal.Scourse, fcomment, fday, fmonth, fyear, ftime, dep_result, anx_result, stress_result, dep_score, anx_score, stress_score, student_form.form_id FROM student_form INNER JOIN student_portal ON student_form.student_id = student_portal.student_id ORDER BY student_form.form_id DESC")
    student_form = cursor.fetchall()

    # Render counselor_dash.html with updated data
    return render_template('counselor_dash.html', data=student_form)

# Scheduling session for student


@app.route('/schedule_ses', methods=['GET', 'POST'])
def goto_scheduling_session():
    if request.method == 'POST':
        student_em = request.form.get('student_email')
        session['id_std'] = student_em

        Date = request.form.get('Date')
        Time = request.form.get('Time')

        formatted_date = datetime.strptime(Date, '%Y-%m-%d').strftime('%B %d, %Y')

        formatted_time = datetime.strptime(Time, '%H:%M').strftime('%I:%M %p')

        print("Student Email:", student_em)
        print("Date:", formatted_date)
        print("Time:", formatted_time)

        try:
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT Sfirst_name FROM student_portal WHERE Semail = %s", (student_em,))
            student_name = cursor.fetchone()[0]

            cursor.execute("INSERT INTO session_record (set_date, set_time, session_email, student_name) VALUES (%s, %s, %s, %s)",
                           (formatted_date, formatted_time, student_em, student_name))
            mysql.connection.commit()
            cursor.close()
            print("Record inserted successfully")

            sender_email = 'jega.mariano.ui@phinmaed.com'
            receiver_email = student_em
            password = 'tzcl uhgq ezme nazq'

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = 'Mental Thrive Schedule Session'

            body = f"Good day, {student_name}. \n\nThis is from the UI Guidance office. I see that you seem to be experiencing something profound based on the results I observed from the form. \nWith that, I wish to meet you regarding it. Don't worry, I will greet you in your current state. \n\nI am looking forward to your coming as I have this day and time scheduled. \n\nYour appointed time is {
                formatted_time} on {formatted_date} \n\nHave a great day!"
            message.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            server.quit()

            print("Email has been sent to " + receiver_email)

            return redirect(url_for('goto_counselor_dash'))

        except Exception as e:
            print("Error inserting record:", e)

    return redirect(url_for('goto_counselor_dash'))


@app.route('/session_history')
def goto_session_history():

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT record_id, session_email, student_name, set_date, set_time, remarks FROM session_record")
    data = cursor.fetchall()

    return render_template('session_history.html', data=data)


@app.route('/remarks', methods=['GET', 'POST'])
def goto_remarks():

    session_idhe = request.form.get('session_idhehe')
    session['id_sesh'] = session_idhe
    print(session_idhe)
    rem = request.form['remark']
    print(rem)

    cursor = mysql.connection.cursor()
    cursor.execute(
        "UPDATE `session_record` SET `remarks`=%s WHERE `record_id` = %s", (rem, session_idhe,))
    # cursor.execute("UPDATE `session_record` SET `remarks` = %s WHERE `record_id` = %s", (rem, record_id))
    mysql.connection.commit()

    session.pop('id_sesh', None)

    return redirect(url_for('goto_session_history'))


@app.route('/view_student_sessions/<student_email>')
def view_student_sessions(student_email):
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT session_email, student_name, set_date, set_time, remarks FROM session_record WHERE session_email = %s", (student_email,))
    student_sessions = cursor.fetchall()
    print(student_email)
    return render_template('student_sessions.html', sessions=student_sessions)


# It will go to counselor charts
@app.route('/counselor_charts')
def goto_counselor_charts():
    selected_course = request.args.get('course')

    cur = mysql.connection.cursor()

    # Fetch available courses with corresponding entries in student_form
    cur.execute("""
        SELECT DISTINCT sp.Scourse 
        FROM student_portal sp
        JOIN student_form sf ON sp.student_id = sf.student_id
    """)
    courses = [course[0] for course in cur.fetchall()]

    query = """
    SELECT dep_result, anx_result, stress_result 
    FROM student_form 
    WHERE student_id IN (
        SELECT student_id FROM student_portal WHERE Scourse = %s
    )
    """ if selected_course else """
    SELECT dep_result, anx_result, stress_result 
    FROM student_form
    """

    cur.execute(query, (selected_course,) if selected_course else ())
    data = cur.fetchall()
    cur.close()

    categorized_data = categorize_data(data)

    return render_template('counselor_charts.html', data=categorized_data, courses=courses, selected_course=selected_course)


def categorize_data(data):
    dep_normal_count = dep_mild_count = dep_moderate_count = dep_severe_count = 0
    anx_normal_count = anx_mild_count = anx_moderate_count = anx_severe_count = 0
    stress_normal_count = stress_mild_count = stress_moderate_count = stress_severe_count = 0

    for dep_result, anx_result, stress_result in data:
        # For Depression
        if dep_result == 'Normal':
            dep_normal_count += 1
        elif dep_result == 'Mild':
            dep_mild_count += 1
        elif dep_result == 'Moderate':
            dep_moderate_count += 1
        elif dep_result == 'Severe':
            dep_severe_count += 1
        elif dep_result == 'Extremely Severe':
            continue  # Skip counting this category

        # For Anxiety
        if anx_result == 'Normal':
            anx_normal_count += 1
        elif anx_result == 'Mild':
            anx_mild_count += 1
        elif anx_result == 'Moderate':
            anx_moderate_count += 1
        elif anx_result == 'Severe':
            anx_severe_count += 1
        elif anx_result == 'Extremely Severe':
            continue  # Skip counting this category

        # For Stress
        if stress_result == 'Normal':
            stress_normal_count += 1
        elif stress_result == 'Mild':
            stress_mild_count += 1
        elif stress_result == 'Moderate':
            stress_moderate_count += 1
        elif stress_result == 'Severe':
            stress_severe_count += 1
        elif stress_result == 'Extremely Severe':
            continue  # Skip counting this category

    categorized_data = {
        'Depression': [
            {'category': 'Normal', 'count': dep_normal_count},
            {'category': 'Mild', 'count': dep_mild_count},
            {'category': 'Moderate', 'count': dep_moderate_count},
            {'category': 'Severe', 'count': dep_severe_count}
        ],
        'Anxiety': [
            {'category': 'Normal', 'count': anx_normal_count},
            {'category': 'Mild', 'count': anx_mild_count},
            {'category': 'Moderate', 'count': anx_moderate_count},
            {'category': 'Severe', 'count': anx_severe_count}
        ],
        'Stress': [
            {'category': 'Normal', 'count': stress_normal_count},
            {'category': 'Mild', 'count': stress_mild_count},
            {'category': 'Moderate', 'count': stress_moderate_count},
            {'category': 'Severe', 'count': stress_severe_count}
        ]
    }

    return categorized_data


#                        "END STATION OF COUNSELOR BUTTON"


#                          "STATION OF STUDENT BUTTON"

# Create class for student login and register
class StudentRegistrationForm(FlaskForm):
    Semail = StringField("", validators=[DataRequired(), Email()])
    Spassword = PasswordField("")
    Sfirst_name = StringField(" ")
    Slast_name = StringField(" ")
    Sid_number = StringField(" ")
    Scourse = SelectField("", choices=[
        ("", "Select Course"),
        ("BSIT", "BSIT (Bachelor of Science in Information Technology)"),
        ("BSN", "BSN (Bachelor of Science in Nursing)"),
        ("BS Pharma", "BS Pharma (Bachelor of Science in Pharmacy)"),
        ("BSA", "BSA (Bachelor of Science in Accountancy)"),
        ("BSAIS", "BSAIS (Bachelor of Science in Accounting Information System)"),
        ("BSBA MM", "BSBA MM (Bachelor of Science in Business Administration major in Marketing Management)"),
        ("BSBA FM", "BSBA FM (Bachelor of Science in Business Administration major in Financial Management)"),
        ("BSHRM", "BSHRM (Bachelor of Science in Hotel & Restaurant Management)"),
        ("BSTM", "BSTM (Bachelor of Science in Tourism Management)"),
        ("BSCE", "BSCE (Bachelor of Science in Civil Engineering)"),
        ("BEED", "BEED (Bachelor of Elementary Education)"),
        ("BSED", "BSED (Bachelor of Secondary Education)"),
        ("BS CRIM", "BS CRIM (Bachelor of Science in Criminology)"),
        ("BSMarE", "BSMarE (Bachelor of Science in Science in Marine Engineering)"),
        ("BSPsych", "BSPsych (Bachelor of Science in in Psychology)"),
        ("BSHM", "BSHM (Bachelor of Science in Hospitality Management)"),
        ("BSME", "BSME (Bachelor of Science in Mechanical Engineering)")], validators=[validators.DataRequired()])
    Signup = SubmitField("Sign up now")


class StudentLoginForm(FlaskForm):
    Semail = StringField(
        "", validators=[DataRequired(), Email(message="Email not Registered")])
    Spassword = PasswordField("")
    Login = SubmitField("Login")


# same goes with COUNSELOR button
@app.route('/student_register', methods=['GET', 'POST'])
def goto_student_register():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        Sfirst_name = form.Sfirst_name.data
        Slast_name = form.Slast_name.data
        Sid_number = form.Sid_number.data
        Scourse = form.Scourse.data
        Semail = form.Semail.data
        Spassword = form.Spassword.data

        pattern = r"^[a-zA-Z0-9._%+-]+.ui@phinmaed.com$"
        hashed_password = bcrypt.generate_password_hash(
            Spassword.encode('utf-8').decode('utf-8'))

        if re.match(pattern, Semail):
            cursor = mysql.connection.cursor()
            cursor.execute(
                " SELECT * FROM mental_thrive.student_portal WHERE Semail = %s", (Semail, ))
            student_check = cursor.fetchone()

            if student_check:
                flash("This email is already taken.")
                return redirect(url_for('goto_student_register'))
            else:
                cursor.execute("INSERT INTO mental_thrive.student_portal (Semail, Spassword, Sfirst_name, Slast_name, Sid_number, Scourse) VALUES (%s, %s, %s, %s, %s, %s )", (
                    Semail, hashed_password, Sfirst_name, Slast_name, Sid_number, Scourse))
                mysql.connection.commit()
                cursor.close()
        else:
            flash("Invalid email! Use your phinmaed email")

        return redirect(url_for('goto_student_register'))

    return render_template('student_registerr.html', form=form)

# for student login


@app.route('/student_login', methods=['GET', 'POST'])
def goto_student_login():
    form = StudentLoginForm()
    if form.validate_on_submit():
        session['Semail'] = request.form['Semail']
        Semail = form.Semail.data
        Spassword = form.Spassword.data

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT student_id, Spassword FROM mental_thrive.student_portal WHERE Semail=%s", (Semail, ))
        student_result = cursor.fetchone()
        cursor.close()

        if student_result and bcrypt.check_password_hash(student_result[1], Spassword.encode('utf-8').decode('utf-8')):
            session['student_id'] = student_result[0]
            return redirect(url_for('goto_student_landingpage'))
        else:
            flash("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_student_login'))

    return render_template('student_login.html', form=form)


password_reset_tokens = {}


@app.route('/forgot_password_student', methods=['GET', 'POST'])
def goto_forgot_password_student():
    if request.method == 'POST':
        email = request.form['email']

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT Semail, Spassword FROM student_portal WHERE Semail = %s", (email,))
        user_reset = cursor.fetchone()

        if user_reset:
            token = secrets.token_urlsafe(16)  # Generate a secure random token

            # Store the token in the database
            cursor.execute(
                "UPDATE student_portal SET reset_token = %s WHERE Semail = %s", (token, email))
            mysql.connection.commit()

            # Send email with password reset link
            send_reset_password_email(email, token)

            print(
                'An email with instructions to reset your password has been sent to your email address.')
            return redirect(url_for('goto_student_login'))
        else:
            print('Email address not found. Please try again.')

    return render_template('forgot_password_student.html')


def send_reset_password_email(email, token):
    sender_email = 'kypa.pama.ui@phinmaed.com'  # Sender's email address
    receiver_email = email
    subject = 'Mental Thrive Password Reset'
    body = f"Reset Your Password\nStudent\nClick the following link to reset your password: {
        url_for('goto_reset_password_student', token=token, _external=True)}"

    # Create message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, 'lbpf kjng bngw uvco')
        server.sendmail(sender_email, receiver_email, message.as_string())


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def goto_reset_password_student(token):
    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password == confirm_password:
            # Fetch email from the database based on the token
            cursor = mysql.connection.cursor()
            cursor.execute(
                "SELECT Semail FROM student_portal WHERE reset_token = %s", (token,))
            ang_email = cursor.fetchone()
            cursor.close()

            if ang_email:
                hashed_password = bcrypt.generate_password_hash(
                    new_password).decode('utf-8')
                # Update password in the database
                cursor = mysql.connection.cursor()
                cursor.execute(
                    "UPDATE student_portal SET Spassword = %s WHERE Semail = %s", (hashed_password, ang_email[0]))
                mysql.connection.commit()
                cursor.close()

                # Redirect to login page after password reset
                return redirect(url_for('goto_student_login'))
            else:
                flash(
                    'Invalid or expired token. Please request a new password reset link.', 'error')
        else:
            flash('Passwords do not match. Please try again.', 'error')

    # If password reset fails, render the reset password page again
    return render_template('reset_password_student.html', token=token)


@app.route('/student_logout')
def goto_student_logout():
    session.pop('student_id', None)
    return redirect(url_for('goto_student_login'))

# It will go to student landing page


@app.route('/student_landingpage')
def goto_student_landingpage():
    if 'student_id' not in session:
        return redirect(url_for('goto_student_login'))

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    student_name = cursor.fetchone()

    titletips = ["Set Clear Goals:", "Break Tasks into Manageable Steps:",
                 "Celebrate Progress:", "Surround Yourself with Positivity:", "Practice Self-Care:"]
    rantips = random.choice(titletips)
    indxtips = titletips.index(rantips)
    tips = ["Define specific, measurable, achievable, relevant, and time-bound (SMART) goals. Having a clear sense of purpose and direction can provide motivation and focus.",
            "Large tasks can be overwhelming. Break them down into smaller, more manageable steps. Achieving these smaller goals provides a sense of accomplishment and motivates you to tackle the next one.",
            "Acknowledge and celebrate your achievements, no matter how small. Recognizing your progress reinforces a positive mindset and encourages continued effort.",
            "Surround yourself with positive influences, whether it's supportive friends and family, inspirational quotes, or uplifting music. Positive environments can contribute to a more optimistic outlook.",
            "Take care of your physical and mental well-being. Ensure you get enough rest, eat nutritious meals, exercise regularly, and make time for activities you enjoy. A healthy body and mind contribute to increased motivation and resilience."]

    resulttitle = rantips
    result = tips[indxtips]

    return render_template('student_landingpage.html', student_name=student_name, resulttitle=resulttitle, result=result)


# It will go to student dashboard
@app.route('/student_dash')
def goto_student_dash():

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT student_portal.Sfirst_name, student_form.fcomment, student_form.fday, student_form.fmonth, student_form.fyear, student_form.ftime, student_form.dep_result, student_form.anx_result, student_form.stress_result, student_form.dep_score, student_form.anx_score, student_form.stress_score FROM student_portal INNER JOIN student_form ON student_portal.student_id = student_form.student_id WHERE student_portal.student_id = %s", (session['student_id'],))
    student_form_records = cursor.fetchall()

    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    student_name = cursor.fetchone()
    cursor.close()

    return render_template('student_dash.html', student_data=student_form_records, student_name=student_name)


@app.route('/student_form', methods=['GET', 'POST'])
def goto_student_form():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM mental_thrive.student_form WHERE student_id = %s AND fyear = %s AND fmonth = %s AND fday = %s",
                   (session['student_id'], date.today().year, date.today().month, date.today().day))
    count_ang_submit = cursor.fetchone()[0]
    cursor.close()

    if count_ang_submit >= 1:
        flash("Daily limit reached! Comeback tomorrow")
        return redirect(url_for('goto_student_landingpage'))

    if request.method == 'POST':
        set_date = request.form['set_date']
        set_time = request.form['set_time']
        fcomment = request.form['fcomment']
        now = datetime.now()
        fday = now.strftime("%d")
        fmonth = now.strftime("%m")
        fyear = now.strftime("%Y")
        ftime = now.strftime("%I:%M %p")

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO mental_thrive.student_form (fcomment, fday, fmonth, fyear, ftime, set_date, set_time) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (fcomment, fday, fmonth, fyear, ftime, set_time, set_date))
        mysql.connection.commit()

        cursor.close()

    # Fetch student name
    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_portal.student_id = %s", (session['student_id'], ))
    student_name = cursor.fetchone()

    RRid = cursor.lastrowid

    # Store the Rid in the session
    session['RRid'] = RRid
    cursor.close()

    # Check if Rid is stored in the session
    if 'RRid' in session:
        print("Rid stored in session:", session['RRid'])
    else:
        print("Rid not found in session.")

    return render_template('student_form.html', student_name=student_name)


@app.route('/success_student', methods=['GET', 'POST'])
def goto_success_student():

    fcomment = request.form['fcomment']
    now = datetime.now()
    fday = now.strftime("%d")
    fmonth = now.strftime("%m")
    fyear = now.strftime("%Y")
    ftime = now.strftime("%I:%M %p")

    Q1 = request.form['Answer1']
    Q2 = request.form['Answer2']
    Q3 = request.form['Answer3']
    Q4 = request.form['Answer4']
    Q5 = request.form['Answer5']
    Q6 = request.form['Answer6']
    Q7 = request.form['Answer7']
    Q8 = request.form['Answer8']
    Q9 = request.form['Answer9']
    Q10 = request.form['Answer10']
    Q11 = request.form['Answer11']
    Q12 = request.form['Answer12']
    Q13 = request.form['Answer13']
    Q14 = request.form['Answer14']
    Q15 = request.form['Answer15']
    Q16 = request.form['Answer16']
    Q17 = request.form['Answer17']
    Q18 = request.form['Answer18']
    Q19 = request.form['Answer19']
    Q20 = request.form['Answer20']
    Q21 = request.form['Answer21']
    Q22 = request.form['Answer22']
    Q23 = request.form['Answer23']
    Q24 = request.form['Answer24']
    Q25 = request.form['Answer25']
    Q26 = request.form['Answer26']
    Q27 = request.form['Answer27']
    Q28 = request.form['Answer28']
    Q29 = request.form['Answer29']
    Q30 = request.form['Answer30']

    # Deppression
    Dep = (int(Q3)+int(Q5)+int(Q10)+int(Q13)+int(Q16) +
           int(Q17)+int(Q21)+int(Q25)+int(Q27)+int(Q29))
    # Anxiety
    Anx = (int(Q2)+int(Q4)+int(Q7)+int(Q9)+int(Q15) +
           int(Q19)+int(Q20)+int(Q22))+int(Q26)+int(Q30)
    # Stress
    Stres = (int(Q1)+int(Q6)+int(Q8)+int(Q11)+int(Q12) +
             int(Q14)+int(Q18)+int(Q23)+int(Q24)+int(Q28))

    if (Dep <= 7):
        Dep_say = "Normal"
        Dep_tip = "It's wonderful to see you embracing life! Keep moving forward, and remember that every step counts."
    elif (Dep <= 14):
        Dep_say = "Mild"
    elif (Dep <= 22):
        Dep_say = "Moderate"
    elif (Dep <= 30):
        Dep_say = "Severe"

    if (Dep >= 8):
        Dep_rand = ["Be more active: Try exercise today!", "Face your fears.", "Eat a healthy diet: Consider what you eat.",
                    "Establish a routine: Create a good routine and stick with it as much as possible.", "Seek help for depression."]
        Dep_tip = random.choice(Dep_rand)

    if (Anx <= 7):
        Anx_say = "Normal"
        Anx_tip = "Life is full of uncertainties, but your ability to stay present is commendable. Keep engaging with the present moment."
    elif (Anx <= 14):
        Anx_say = "Mild"
    elif (Anx <= 22):
        Anx_say = "Moderate"
    elif (Anx <= 30):
        Anx_say = "Severe"

    if (Anx >= 8):
        Anx_rand = ["Question your thought pattern: Challenge your fears, ask if they’re true, and see where you can regain control.", "Practice focused, deep breathing: Breathing in for 4 counts and breathing out for 4 counts for 5 minutes total. ",
                    "Try aromatherapy: Lit scented candles or incense like lavender candle and sandalwood.", "Exercise: Walk or do a yoga.", "Grounding Techniques: Naming three things you can see, three sounds you can hear, and interacting with three things you can touch."]
        Anx_tip = random.choice(Anx_rand)

    if (Stres <= 7):
        Stres_say = "Normal"
        Stres_tip = "Balancing life can be tricky, but your efforts are noticeable. Take breaks, prioritize self-care, and remember, you're doing well."
    elif (Stres <= 14):
        Stres_say = "Mild"
    elif (Stres <= 22):
        Stres_say = "Moderate"
    elif (Stres <= 30):
        Stres_say = "Severe"

    if (Stres >= 8):
        Stres_rand = ["Setting aside 10 minutes a day to relax and collect my thoughts.", "Writing a letter to someone to get your feelings across and vent, but not actually sending it.",
                      "Spend time with positive people around you.", "Play a musical instrument.", "Eat or drink something you enjoy."]
        Stres_tip = random.choice(Stres_rand)

    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO mental_thrive.student_form (fcomment, fday, fmonth, fyear, ftime, dep_score, anx_score, stress_score, dep_result, anx_result, stress_result, student_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (fcomment, fday, fmonth, fyear, ftime, Dep, Anx, Stres, Dep_say, Anx_say, Stres_say, session['student_id'], ))
    mysql.connection.commit()

    # Get the Rid of the newly inserted record
    form_id = cursor.lastrowid

    # Store the Rid in the session
    session['form_id'] = form_id

    cursor.close()

    return render_template('success_student.html', Dep=Dep, Anx=Anx, Stres=Stres,
                           Dep_say=Dep_say, Anx_say=Anx_say, Stres_say=Stres_say, Dep_tip=Dep_tip, Anx_tip=Anx_tip,
                           Stres_tip=Stres_tip)


# I will go to student charts
@app.route('/student_charts')
def goto_student_charts():
    cursor = mysql.connection.cursor()

    # Fetching student-specific data
    cursor.execute(
        "SELECT dep_result,anx_result,stress_result FROM student_portal INNER JOIN student_form ON student_portal.student_id = student_form.student_id WHERE student_portal.student_id = %s", (session['student_id'],))
    data = cursor.fetchall()

    # Fetching student's name
    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'],))
    student_name = cursor.fetchone()
    cursor.close()

    # Categorizing the fetched data
    categorized_data = categorize_data(data)

    return render_template('student_charts.html', data=categorized_data, student_name=student_name)


def categorize_data(data):
    dep_normal_count = dep_mild_count = dep_moderate_count = dep_severe_count = dep_extremely_severe = 0
    anx_normal_count = anx_mild_count = anx_moderate_count = anx_severe_count = anx_extremely_severe = 0
    stress_normal_count = stress_mild_count = stress_moderate_count = stress_severe_count = stress_extremely_severe = 0

    for dep_result, anx_result, stress_result in data:
        # For Depression
        if dep_result == 'Normal':
            dep_normal_count += 1
        elif dep_result == 'Mild':
            dep_mild_count += 1
        elif dep_result == 'Moderate':
            dep_moderate_count += 1
        elif dep_result == 'Severe':
            dep_severe_count += 1
        elif dep_result == 'Extremely Severe':
            dep_extremely_severe += 1

        # For Anxiety
        if anx_result == 'Normal':
            anx_normal_count += 1
        elif anx_result == 'Mild':
            anx_mild_count += 1
        elif anx_result == 'Moderate':
            anx_moderate_count += 1
        elif anx_result == 'Severe':
            anx_severe_count += 1
        elif anx_result == 'Extremely Severe':
            anx_extremely_severe += 1

        # For Stress
        if stress_result == 'Normal':
            stress_normal_count += 1
        elif stress_result == 'Mild':
            stress_mild_count += 1
        elif stress_result == 'Moderate':
            stress_moderate_count += 1
        elif stress_result == 'Severe':
            stress_severe_count += 1
        elif stress_result == 'Extremely Severe':
            stress_extremely_severe += 1

    categorized_data = {
        'Depression': [
            {'category': 'Normal', 'count': dep_normal_count},
            {'category': 'Mild', 'count': dep_mild_count},
            {'category': 'Moderate', 'count': dep_moderate_count},
            {'category': 'Severe', 'count': dep_severe_count},
            {'category': 'Extremely Severe', 'count': dep_extremely_severe}
        ],

        'Anxiety': [
            {'category': 'Normal', 'count': anx_normal_count},
            {'category': 'Mild', 'count': anx_mild_count},
            {'category': 'Moderate', 'count': anx_moderate_count},
            {'category': 'Severe', 'count': anx_severe_count},
            {'category': 'Extremely Severe', 'count': anx_extremely_severe}
        ],

        'Stress': [
            {'category': 'Normal', 'count': stress_normal_count},
            {'category': 'Mild', 'count': stress_mild_count},
            {'category': 'Moderate', 'count': stress_moderate_count},
            {'category': 'Severe', 'count': stress_severe_count},
            {'category': 'Extremely Severe', 'count': stress_extremely_severe}
        ]
    }

    print(categorized_data)

    return categorized_data


# I will go to student profile
@app.route('/student_profile')
def goto_student_profile():
    cursor = mysql.connection.cursor()

    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    student_name = cursor.fetchone()

    # cursor.execute("SELECT Sid_number, Semail, Sfirst_name, Slast_name, Scourse FROM student_portal ")
    # profile = cursor.fetchall()

    cursor.execute(
        "SELECT Sid_number FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    idnum = cursor.fetchone()

    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    fname = cursor.fetchone()

    cursor.execute(
        "SELECT Slast_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    lname = cursor.fetchone()

    cursor.execute(
        "SELECT Scourse FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    course = cursor.fetchone()

    cursor.execute(
        "SELECT Semail FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    email = cursor.fetchone()
    cursor.close()

    return render_template('student_profile.html', student_name=student_name, idnum=idnum, fname=fname, lname=lname, course=course, email=email)


@app.route('/student_session_history')
def goto_student_session_history():

    student_emai = session['Semail']

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT student_name, set_date, set_time, remarks FROM session_record WHERE session_email = %s", (student_emai,))
    ses_ni_student = cursor.fetchall()

    cursor.execute(
        "SELECT Sfirst_name FROM student_portal WHERE student_id = %s", (session['student_id'], ))
    student_name = cursor.fetchone()
    cursor.close()

    return render_template('student_session_history.html', ses_ni_student=ses_ni_student, student_name=student_name)


#                         "END STATION OF STUDENT BUTTON"


#                          "STATION OF ADMINISTRATION BUTTON"

class AdminRegistrationForm(FlaskForm):
    Aemail = StringField("", validators=[DataRequired(), Email()])
    Apassword = PasswordField("", validators=[DataRequired()])
    Login = SubmitField("Login")


@app.route('/confirm_counselor', methods=['POST'])
def goto_confirm_counselor():
    counselor_id = request.form.get('counselor_id')

    cursor = mysql.connection.cursor()

    try:
        update_counselor_account = "UPDATE counselor_portal SET status = 1 WHERE counselor_id = %s"
        cursor.execute(update_counselor_account, [counselor_id])
        mysql.connection.commit()
        print('Counselor account confirmed successfully!')
    except Exception as e:
        print(e)
        print('Failed to confirm counselor account.')
    finally:
        cursor.close()

    return redirect(url_for('goto_admin_counselors'))


@app.route('/administration_login', methods=['GET', 'POST'])
def goto_administration_login():
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        Aemail = form.Aemail.data
        Apassword = form.Apassword.data

        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT Apassword FROM mental_thrive.admin_portal WHERE Aemail = %s", (Aemail, ))
        admin_check = cursor.fetchone()
        cursor.close()

        if admin_check:
            session['student_id'] = admin_check[0]
            return redirect(url_for('goto_administration_dash'))
        else:
            flash("Invalid Credentials! Please try again.")
            return redirect(url_for('goto_administration_login'))

    return render_template('administration_login.html', form=form)


@app.route('/admin_counselors')
def goto_admin_counselors():

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT counselor_id, Cemail, Cpassword FROM mental_thrive.counselor_portal")
    counselor_account = cursor.fetchall()

    return render_template('admin_counselors.html', counselor_data=counselor_account)


@app.route('/admin_students')
def goto_admin_students():

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT student_id, Semail, Sfirst_name, Slast_name, Sid_number, Scourse, Spassword FROM mental_thrive.student_portal")
    student_account = cursor.fetchall()

    return render_template('admin_students.html', student_dataz=student_account)


@app.route('/admin_dash')
def goto_administration_dash():

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT student_portal.Sfirst_name, student_portal.Scourse, fcomment, fday, ftime, fmonth, fyear, dep_result, anx_result, stress_result, dep_score, anx_score, stress_score FROM student_form INNER JOIN student_portal ON student_form.student_id = student_portal.student_id")
    student_form = cursor.fetchall()
    cursor.close()

    return render_template('admin_dash.html', student_data=student_form)


@app.route('/admin_charts')
def goto_admin_charts():
    selected_course = request.args.get('course')

    cur = mysql.connection.cursor()

    # Fetch available courses with corresponding entries in student_form
    cur.execute("""
        SELECT DISTINCT sp.Scourse 
        FROM student_portal sp
        JOIN student_form sf ON sp.student_id = sf.student_id
    """)
    courses = [course[0] for course in cur.fetchall()]

    query = """
    SELECT dep_result, anx_result, stress_result 
    FROM student_form 
    WHERE student_id IN (
        SELECT student_id FROM student_portal WHERE Scourse = %s
    )
    """ if selected_course else """
    SELECT dep_result, anx_result, stress_result 
    FROM student_form
    """

    cur.execute(query, (selected_course,) if selected_course else ())
    data = cur.fetchall()
    cur.close()

    categorized_data = categorize_data(data)

    return render_template('admin_charts.html', data=categorized_data, courses=courses, selected_course=selected_course)


def categorize_data(data):
    dep_normal_count = dep_mild_count = dep_moderate_count = dep_severe_count = 0
    anx_normal_count = anx_mild_count = anx_moderate_count = anx_severe_count = 0
    stress_normal_count = stress_mild_count = stress_moderate_count = stress_severe_count = 0

    for dep_result, anx_result, stress_result in data:
        # For Depression
        if dep_result == 'Normal':
            dep_normal_count += 1
        elif dep_result == 'Mild':
            dep_mild_count += 1
        elif dep_result == 'Moderate':
            dep_moderate_count += 1
        elif dep_result == 'Severe':
            dep_severe_count += 1
        elif dep_result == 'Extremely Severe':
            continue  # Skip counting this category

        # For Anxiety
        if anx_result == 'Normal':
            anx_normal_count += 1
        elif anx_result == 'Mild':
            anx_mild_count += 1
        elif anx_result == 'Moderate':
            anx_moderate_count += 1
        elif anx_result == 'Severe':
            anx_severe_count += 1
        elif anx_result == 'Extremely Severe':
            continue  # Skip counting this category

        # For Stress
        if stress_result == 'Normal':
            stress_normal_count += 1
        elif stress_result == 'Mild':
            stress_mild_count += 1
        elif stress_result == 'Moderate':
            stress_moderate_count += 1
        elif stress_result == 'Severe':
            stress_severe_count += 1
        elif stress_result == 'Extremely Severe':
            continue  # Skip counting this category

    categorized_data = {
        'Depression': [
            {'category': 'Normal', 'count': dep_normal_count},
            {'category': 'Mild', 'count': dep_mild_count},
            {'category': 'Moderate', 'count': dep_moderate_count},
            {'category': 'Severe', 'count': dep_severe_count}
        ],
        'Anxiety': [
            {'category': 'Normal', 'count': anx_normal_count},
            {'category': 'Mild', 'count': anx_mild_count},
            {'category': 'Moderate', 'count': anx_moderate_count},
            {'category': 'Severe', 'count': anx_severe_count}
        ],
        'Stress': [
            {'category': 'Normal', 'count': stress_normal_count},
            {'category': 'Mild', 'count': stress_mild_count},
            {'category': 'Moderate', 'count': stress_moderate_count},
            {'category': 'Severe', 'count': stress_severe_count}
        ]
    }

    return categorized_data

#                         "END STATION OF ADMINISTRATION BUTTON"


if __name__ == '__main__':
    app.run(debug=True, port=8080)
