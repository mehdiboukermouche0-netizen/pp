# مثال باستخدام Flask
from flask import Flask, render_template, request, jsonify, session
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class Student:
    def __init__(self, id, name, institution, phone, whatsapp, email, birthdate, grade):
        self.id = id
        self.name = name
        self.institution = institution
        self.phone = phone
        self.whatsapp = whatsapp
        self.email = email
        self.birthdate = birthdate
        self.grade = grade

class AttendanceSystem:
    def __init__(self):
        self.students = []
        self.attendance_records = {}
        self.load_data()
    
    def add_student(self, name, institution, phone, whatsapp, email, birthdate, grade):
        new_id = len(self.students) + 1
        student = Student(new_id, name, institution, phone, whatsapp, email, birthdate, grade)
        self.students.append(student)
        self.save_data()
        return student
    
    def record_attendance(self, student_id, date, status):
        if date not in self.attendance_records:
            self.attendance_records[date] = {}
        self.attendance_records[date][student_id] = status
        self.save_data()
    
    def get_student_stats(self, student_id):
        # حساب إحصائيات الطالب
        pass
    
    def load_data(self):
        # تحميل البيانات من ملف
        pass
    
    def save_data(self):
        # حفظ البيانات في ملف
        pass

# تهيئة النظام
attendance_system = AttendanceSystem()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        data = request.json
        student = attendance_system.add_student(
            data['name'],
            data['institution'],
            data['phone'],
            data['whatsapp'],
            data['email'],
            data['birthdate'],
            data['grade']
        )
        return jsonify({'success': True, 'student': student.__dict__})
    
    students_data = [s.__dict__ for s in attendance_system.students]
    return jsonify(students_data)

@app.route('/api/attendance', methods=['POST'])
def record_attendance():
    data = request.json
    attendance_system.record_attendance(
        data['student_id'],
        data['date'],
        data['status']
    )
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)
