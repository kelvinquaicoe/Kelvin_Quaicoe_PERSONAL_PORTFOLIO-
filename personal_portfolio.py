
#1  Personal Information Storage
Full_name= ('Kelvin Quaicoe')
Student_email= ('kkquaicoe@ncat.edu') 
Hometown= ('Charlotte, NC')
Graduation_semester= ('Spring 2028') 
Major= ('Computer Science')

#2  list
Current_courses= ['COMP 163', 'MATH 150', 'MNGT 101', 'HIS 105','COM 180']
Completed_courses = ['Biology', 'Chemistry', 'Calculus'', Spanish II', 'World History'] 
Credit_hours= [3, 3, 3, 3,3]
GPA_history= [4, 4, 3.9, 3.75,4]

#3  tuple
Emergency_contact= ('Mom', 'Fafa Asiseh', '704-555-0199')
Home_address= ('5711 Fountain Head Drive', 'Charlotte', 'NC', '25455')
Instagram_info= ('Instagram', '@KKQ', 500)
Twitter_info= ('Twitter', '@KKQ',2 )
Birthday= ('Birthday', 7, 10, 2003  )

#4  set
Current_skills= {'Python basics', 'HTML', 'Problem solving', 'Time management', 'Photography'}
Skills_to_learn= {'JavaScript', 'Data structures', 'Git', 'Web design', 'Public speaking'} 
Career_interests= {'Software development', 'Web development', 'Data science', 'Game development'} 
Hobbies= {'Volleyball', 'Music'} 
Entertainment_backlog= {'One Piece', 'Barry'}

#5  dictionary
Course_credits= {'COMP 163': 3, 'MATH 150': 3, 'MNGT 101': 3, 'HIS 105': 3,'COM 180': 3 }
Course_professors= {'COMP 163': 'Prof. Rhodes', 'MATH 150': 'Dr. Lee', 'MNGT 101': 'Dr. Martinez', 'HIS 105': 'Dr. Brown','COM 180': 'Dr. Gyasi'}
Course_rooms= {'COMP 163': 'M-Eric 300', 'MATH 150': 'Marteena 201', 'ENG 101': 'Crosby 121', 'HIS 105': 'Crosby 210' }
Monthly_budget= {'Food': 450, 'Entertainment': 20, 'Books': 0, 'Transportation': 50} 
Study_hrs_per_sub= {'Programming': 10, 'Math': 8, 'Management': 4, 'History': 3, 'Discrete math':  5} 
Contact_directory= {'Aunt': '704-555-0199', 'Roommate': '336-5557821', 'Academic Advisor': '336-334-5000'}

#6 Required Calculations
Total_current_credits= sum(Credit_hours)
Cumulative_GPA= sum(GPA_history)/len(GPA_history)
completed_courses= len(Completed_courses)
Total_wkly_study_hrs= sum(Study_hrs_per_sub.values())
Academic_load= Total_current_credits + Total_wkly_study_hrs
Monthly_budget_total= sum(Monthly_budget.values())
Daily_food_budget= (Monthly_budget['Food']/30)
Daily_food_budget= round(Daily_food_budget,2)
Annual_budget_projection= Monthly_budget_total * 12
Study_cost_per_hour= (Monthly_budget['Books'])/Total_wkly_study_hrs
Study_cost_per_hour= round(Study_cost_per_hour,2)

#7 Analytics Calculations
social_media_followers= (Instagram_info[2])+(Twitter_info[2])
Skills_count_comparison= f'{len(Current_skills)} Vs {len(Skills_to_learn)}'
Contact_directory_size= len(Contact_directory)
Entertainment_backlog_management= len(Entertainment_backlog)
Academic_workload_assessment = Academic_load

print('================================================================')
print('              PERSONAL ACADEMIC & LIFE PORTFOLIO')
print('================================================================')
print(f'Student: {Full_name} | Email: {Student_email}')
print(f'From: {Hometown} | Graduating: {Graduation_semester}')
print(f'Major: {Major}')

print(f'\n=== ACADEMIC PROFILE ===')
print(f'Current Semester: {Total_current_credits} credits across 4 courses')
print(f'Cumulative GPA: {Cumulative_GPA:.2f}')
print(f'Weekly Study Time: {Total_wkly_study_hrs} hours')
print(f'Academic Investment: ${Study_cost_per_hour:.1f} per study hour')

print(f'\nCurrent Courses:')
print(f'COMP 163 - {Course_credits['COMP 163']} credits -{Course_professors['COMP 163']} - {Course_rooms['COMP 163']}')
print(f'MATH 150 - {Course_credits['MATH 150']} credits -{Course_professors['MATH 150']} - {Course_rooms['MATH 150']}')
print(f'ENG 101 -  {Course_credits['ENG 101']} credits -{Course_professors['ENG 101']} - {Course_rooms['ENG 101']}')
print(f'HIS 105 - {Course_credits['HIS 105']} credits -{Course_professors['HIS 105']} - {Course_rooms['HIS 105']}')

print(f'\n=== PERSONAL DEVELOPMENT ===')
print(f'Current Skills: {Current_skills}')
print(f'Learning Goals: {Skills_to_learn}')
print(f'Career Interests: {Career_interests}')
print(f'Skills Currently Have: {len(Current_skills)}')
print(f'Skills Want to Learn: {len(Skills_to_learn)}')

print(f'\n=== FINANCIAL OVERVIEW ===')
print(f'Monthly Budget: ${Monthly_budget_total}')
print(f'Food: ${Monthly_budget['Food']} (${Daily_food_budget}/day)')
print(f'Entertainment: ${Monthly_budget['Entertainment']}')
print(f'Books: ${Monthly_budget['Books']}')
print(f'Transportation: ${Monthly_budget['Transportation']}')
print(f'Annual Projection: ${Monthly_budget_total*12}')

print(f'\n=== CONNECTIONS & CONTACTS ===')
print(f'Emergency Contact: {Emergency_contact[1]} ({Emergency_contact[0]}) - {Emergency_contact[2]}')
print(f'Home Address: {Home_address[0]}, {Home_address[1]}, {Home_address[2]} {Home_address[3]}')
print(f'Social Media Presence: {social_media_followers} followers across 2 platforms')
print(f'Key Contacts: {Contact_directory_size} people in directory')

print(f'\n=== LIFE STATISTICS ===')
print(f'Total Courses Completed: {completed_courses}')
print(f'Current Academic Load: {Academic_load} weekly commitments')
print(f'Entertainment Backlog: {Entertainment_backlog_management} items')
print(f'Current Hobbies: {len(Hobbies)} activities')
print('================================================================')




