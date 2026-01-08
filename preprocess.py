import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm

def process_posts(raw_file_path, processed_file_path="Data/preprocessed_post.json"):
    
    enriched_post = []

    with open(raw_file_path, encoding='utf-8') as file:
        posts = json.load(file)
        for post in posts:
           metadata = extract_metadata(post['text'])

           post_with_metadata = post | metadata
           enriched_post.append(post_with_metadata)

           post = {'text':'abcd', 'engagement':369}
           metadata = {'line_count':10, 'language':'English','tags':['Mental Health','Motivation']}
   
    Unified_tags = get_unified_tags(enriched_post)

    for post in enriched_post:
        current_tags = post['tags']
        new_tags = {Unified_tags[tag] for tag in current_tags}
        post['tags'] = list(new_tags)

    with open(processed_file_path, encoding='utf-8', mode="w") as outfile:
        json.dump(enriched_post, outfile, indent=4)
        

def get_unified_tags(post_with_metadata):
    Unique_tags =  set()
    
    for post in post_with_metadata:
        Unique_tags.update(post['tags'])
    unique_tags_list = ','.join(Unique_tags)

    PROMPT = ''' I will give you a list of tags. You need to unify tags with the following requirements,
    1. Tags are unified and marged to create a shorter list.
       Example 1: "Jobseekers", "Job Hunting", "Job Finding" can be all merged into a single tag "Job Search".
       Example 2: "Career Growth", "Career Development", "Career Progression" can be all merged into a single tag " Career Growth". 
       Example 3: "Resume", "CV", "Cover Letter" can be all merged into a single tag "Resume & CV".
       Example 4: "Interview", "Interview Preparation", "Mock Interview" can be all merged into a single tag " Interview Prep".
       Example 5: "Web Development", "Frontend", "Backend", "Full Stack" can be all merged into a single tag "Web Development".
       Example 6: "Coding", "Programming", "Software Development" can be all merged into a single tag "Software Engineering".
       Example 7: "Online Course", "E-learning", "Self Learning" can be all merged into a single tag "Online Learning".
       Example 8: "Campus Placement", "College Placement", "On-Campus Hiring" can be all merged into a single tag "Campus Placement". 
       Example 9: "Internship", "Intern", "Industrial Training" can be all merged into a single tag "Internships".
       Example 10: "Generative AI", "GenAI", "LLMs" can be all merged into a single tag "Gen AI".
    2. Each tag should be follow title case convention. example: "Motivation", "Job Search"
    3. Output should be a JSON object, No Preamble
    4. Output should have mapping of original tag and the unified tag.
        For example: {{"Jobseeker":"Job Search", "Job Hunting":"Job Search", "Motivation":"Motivation"}}

    Here is the list of tags:
    {tags}
    '''

    pt = PromptTemplate.from_template(PROMPT)
    chain = pt | llm
    response = chain.invoke(input={'tags': str(unique_tags_list)})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res


def extract_metadata(post):

    PROMPT = '''
    You are given a Linkdin Post. You need to extract number of lines, language of the post and tags.
    1. Return a valid JSON. No preamble.
    2. JSON object should have exactly three keys: line_count, language and tags.
    3. tags is an array of text tags. Extract maximum two tags.
    4. The language of the post must be either:
       English, or 
       Hinglish (Hindi words written using English letters mixed with English).
       Do not use Hindi script or any other language.

    Here is the actual post on which you need to perform this task:
    {post}
    '''

    pt = PromptTemplate.from_template(PROMPT)
    chain = pt | llm
    response = chain.invoke(input={'post': post})

    try:
        json_parser = JsonOutputParser()
        res = json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException("Context too big. Unable to parse jobs.")
    return res

if __name__=="__main__":
    process_posts("Data/raw_post.json", "Data/preprocessed_post.json")