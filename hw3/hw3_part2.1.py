

import json
import os

def generate_dot_code(course_data, prerequisites_data):
    allowed_subjects = ['CSCI', 'MATH']
    dot_code = "digraph CoursePrerequisites {\n"
    crn_to_course_name = {}

    for subject_data in course_data:
        subject_code = subject_data.get('code', '')
        courses = subject_data.get('courses', [])

        if subject_code not in allowed_subjects:
            continue

        for course_info in courses:
            if 'crse' not in course_info or 'id' not in course_info or 'title' not in course_info or 'sections' not in course_info:
                continue

            course_id = str(course_info['crse'])
            course_name = course_info['id']
            title = course_info['title']

            crn = course_info['sections'][0].get('crn', '')
            crn_to_course_name[crn] = course_name

            if 'instructor' in course_info['sections'][0]:
                professor = course_info['sections'][0]['instructor']
            else:
                professor = "Unknown"

            subject = course_info.get('subj', "Unknown")
            crn = course_info['sections'][0].get('crn', '')
            print(crn)

            prerequisites_info = prerequisites_data.get(str(crn), {}).get('prerequisites', {})
            # print(prerequisites_data.get(str(crn)))
            prerequisite_code = extract_prerequisite_code(prerequisites_info)
            # print(prerequisites_info)
            # print(prerequisite_code)

            dot_code += f'  {course_name} [label="{title}\n({course_name})\\nProf: {professor}\\nSubject: {subject}\\nCRSE: {course_id}"]\n'
            dot_code += f'  {prerequisite_code} -> {course_name}\n'

    dot_code += "}\n"
    return dot_code

def extract_prerequisite_code(prerequisites_info):
    if prerequisites_info:
        type = prerequisites_info.get('type', '')
        if type == 'and':
            nested_prerequisites = prerequisites_info.get('nested', [])            
            for nested_item in nested_prerequisites:
                
                print(nested_item) 
                # course_crn = nested_item.get('nested', []).get('course', '')
                # print(course_crn)
        elif type == 'or':
            nested_prerequisites = prerequisites_info.get('nested', [])
            for nested_item in nested_prerequisites:
                pass
        elif type == 'course':
            course_crn = prerequisites_info.get('course', '')
            print(course_crn)
    return ''


if __name__ == "__main__":
    print("Current Working Directory:", os.getcwd())
    with open('/Users/jaeseok/Developer/IV/courses.json', 'r') as course_file:
        course_json = json.load(course_file)

    with open('/Users/jaeseok/Developer/IV/prerequisites.json', 'r') as prerequisite_file:
        prerequisites_json = json.load(prerequisite_file)

    dot_code = generate_dot_code(course_json, prerequisites_json)
    print(dot_code)

    output_file_path = '/Users/jaeseok/Developer/IV/subjects.dot'
    with open(output_file_path, 'w') as output_file:
        output_file.write(dot_code)

    print(f"DOT code written to {output_file_path}")
