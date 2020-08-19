from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)
# Deployment instructions are at:
# https://www.codementor.io/@jqn/deploy-a-flask-app-on-aws-ec2-13hp1ilqy2

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/add')
def add():
   return render_template('add.html')

@app.route('/insert', methods = ['POST', 'GET'])
def insert():
   # define output result dicts
   sse_resource_dict_input = {}
   sse_resource_dict_error = {}
   sse_resource_dict_msg = {}
   # the below list of dicts goes back to add.html (so this is the MODEL of MVC pattern)
   sse_resource_dict_list = [sse_resource_dict_input, sse_resource_dict_msg]
   # start request processing
   if request.method == 'POST':
      try:
         # parse input parameters
         resource_name = request.form['resource_name']
         resource_description = request.form['resource_description']
         resource_details = request.form['resource_details']         
         groups = request.form.getlist('groups')
         values = request.form.getlist('values')
         a_category = request.form['categories']

         if resource_name.strip() == "" or resource_description.strip() == "" or \
            resource_details.strip() == "" or groups == [] or \
            values == []:
            raise Exception("All fields should be filled") 

         ###############################
         # popualte sse_resource_dict_input
         ###############################
         sse_resource_dict_input['resource_name'] = resource_name
         sse_resource_dict_input['resource_description'] = resource_description
         sse_resource_dict_input['resource_details'] = resource_details
         sse_resource_dict_input['groups'] = groups
         sse_resource_dict_input['values'] = values
         sse_resource_dict_input['categories'] = a_category
         # handle groups
         pre_sse_str = 'N'
         group_1_str = 'N'
         group_2_str = 'N'
         group_3_str = 'N'
         group_4_str = 'N'
         for a_group in groups:
            if a_group == 'pre_sse':
               pre_sse_str = 'Y' 
            elif a_group == 'group_1':
               group_1_str = 'Y'
            elif a_group == 'group_2':
               group_2_str = 'Y'
            elif a_group == 'group_3':
               group_3_str = 'Y'
            elif a_group == 'group_4':
               group_4_str = 'Y'
         # handle categories   
         story_str = 'N'
         activity_str = 'N'
         quote_str = 'N'
         life_application_str = 'N'
         role_model_str = 'N'
         ethical_dilemma_str = 'N'
         book_str = 'N'
         if a_category == 'story':
            story_str = 'Y' 
         elif a_category == 'activity':
            activity_str = 'Y'
         elif a_category == 'quote':
            quote_str = 'Y'
         elif a_category == 'life_application':
            life_application_str = 'Y'
         elif a_category == 'role_model':
            role_model_str = 'Y'
         elif a_category == 'ethical_dilemma':
            ethical_dilemma_str = 'Y'
         elif a_category == 'book':
            book_str = 'Y'
         # handle values/sub-values
         truth_str = 'N'
         right_conduct_str = 'N'  
         peace_str = 'N'
         love_str = 'N'
         non_violence_str = 'N'
         self_discipline_str = 'N'
         forbearance_str = 'N'
         duty_str = 'N'
         devotion_str = 'N'
         discrimination_str = 'N'
         determination_str = 'N'
         purity_str = 'N'
         perseverance_str = 'N'
         patience_str = 'N'
         selfless_service_str = 'N'
         honesty_str = 'N'
         compassion_str = 'N'
         forgiveness_str = 'N'
         kindness_str = 'N'
         tolerance_str = 'N'    
         cleanliness_str = 'N'
         contentment_str = 'N'
         courage_str = 'N'
         gratitude_str = 'N'
         sacrifice_str = 'N'
         self_confidence_str = 'N'
         humility_str = 'N'
         self_control_str = 'N'
         ceiling_on_desires_str = 'N'
         unity_in_thought_word_and_deed_str = 'N'
         for a_value in values:
            if a_value == 'truth':
               truth_str = 'Y' 
            elif a_value == 'right_conduct':
               right_conduct_str = 'Y'
            elif a_value == 'peace':
               peace_str = 'Y'
            elif a_value == 'love':
               love_str = 'Y'
            elif a_value == 'non_violence':
               non_violence_str = 'Y'
            elif a_value == 'self_discipline':
               self_discipline_str = 'Y'
            elif a_value == 'forbearance':
               forbearance_str = 'Y'
            elif a_value == 'duty':
               duty_str = 'Y'
            elif a_value == 'devotion':
               devotion_str = 'Y'
            elif a_value == 'discrimination':
               discrimination_str = 'Y'
            elif a_value == 'determination':
               determination_str = 'Y'
            elif a_value == 'purity':
               purity_str = 'Y'
            elif a_value == 'perseverance':
               perseverance_str = 'Y'
            elif a_value == 'patience':
               patience_str = 'Y'
            elif a_value == 'selfless_service':
               selfless_service_str = 'Y'
            elif a_value == 'honesty':
               honesty_str = 'Y'
            elif a_value == 'compassion':
               compassion_str = 'Y'
            elif a_value == 'forgiveness':
               forgiveness_str = 'Y'
            elif a_value == 'kindness':
               kindness_str = 'Y'
            elif a_value == 'tolerance':
               tolerance_str = 'Y'
            elif a_value == 'cleanliness':
               cleanliness_str = 'Y'
            elif a_value == 'contentment':
               contentment_str = 'Y'
            elif a_value == 'courage':
               courage_str = 'Y'
            elif a_value == 'gratitude':
               gratitude_str = 'Y'
            elif a_value == 'sacrifice':
               sacrifice_str = 'Y'
            elif a_value == 'self_confidence':
               self_confidence_str = 'Y'
            elif a_value == 'humility':
               humility_str = 'Y'
            elif a_value == 'self_control':
               self_control_str = 'Y'
            elif a_value == 'ceiling_on_desires':
               ceiling_on_desires_str = 'Y'
            elif a_value == 'unity_in_thought_word_and_deed':
               unity_in_thought_word_and_deed_str = 'Y'

         with sql.connect("sse_resources.db") as con:
         # with sql.connect("/home/ubuntu/sse_resource_repository/sse_resources.db") as con:
            cur = con.cursor()            
            cur.execute("INSERT INTO resources (resource_name, resource_description, resource_details, \
               pre_sse, group_1, group_2, group_3, group_4, story, activity, quote, \
                  life_application, role_model, ethical_dilemma, book, truth, right_conduct, \
                     peace, love, non_violence, self_discipline, forbearance, duty, devotion, \
                        discrimination, determination, purity, perseverance, patience, selfless_service, \
                           honesty, compassion, forgiveness, kindness, tolerance, cleanliness, \
                              contentment, courage, gratitude, sacrifice, self_confidence, \
                                 humility, self_control, ceiling_on_desires, unity_in_thought_word_and_deed)\
                             VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                                ( resource_name, resource_description, resource_details, \
                                   pre_sse_str, group_1_str, group_2_str, group_3_str, group_4_str, \
                                      story_str, activity_str, quote_str, life_application_str, \
                                         role_model_str, ethical_dilemma_str, book_str, truth_str, \
                                            right_conduct_str, peace_str, love_str, non_violence_str, \
                                               self_discipline_str, forbearance_str, duty_str, devotion_str, \
                                                  discrimination_str, determination_str, purity_str, perseverance_str, \
                                                     patience_str, selfless_service_str, honesty_str, \
                                                        compassion_str, forgiveness_str, kindness_str, \
                                                           tolerance_str, cleanliness_str, contentment_str, \
                                                              courage_str, gratitude_str, sacrifice_str, self_confidence_str, \
                                                                 humility_str, self_control_str, ceiling_on_desires_str, \
                                                                    unity_in_thought_word_and_deed_str ) )            
            con.commit()
            sse_resource_dict_msg['msg'] = "Record successfully added"
      except Exception as ex:
         # con.rollback()
         sse_resource_dict_error['error'] = ex
         sse_resource_dict_list = [sse_resource_dict_error, {}]      
      finally:
         # con.close()
         return render_template("result.html",sse_resource_dict_list = sse_resource_dict_list)


@app.route('/search',methods = ['POST', 'GET'])
def search():
   # define output result dicts
   sse_resource_dict_input = {}
   sse_resource_dict_error = {}
   sse_resource_dict_data = {}
   # the below list of dicts goes back to result.html (so this is the MODEL of MVC pattern)
   sse_resource_dict_list = [sse_resource_dict_input, sse_resource_dict_data]
   # start request processing
   if request.method == 'POST':
      try:
         # parse input parameters
         a_group = request.form['groups']
         a_value = request.form['values']
         a_category = request.form['categories']
         ###############################
         # popualte sse_resource_dict_input
         ###############################
         sse_resource_dict_input['groups'] = a_group
         sse_resource_dict_input['values'] = a_value
         sse_resource_dict_input['categories'] = a_category

         con = sql.connect("sse_resources.db")
         # con = sql.connect("/home/ubuntu/sse_resource_repository/sse_resources.db")
         con.row_factory = sql.Row
         query_string = "SELECT resource_name, resource_description, resource_details FROM resources WHERE {g} = 'Y' AND {c} = 'Y' AND {v} = 'Y'".format (g=a_group, c=a_category, v=a_value)         
         cur = con.cursor()
         cur.execute(query_string)         
         rows = cur.fetchall()
         sse_resource_dict_data['resultset'] = rows
      except Exception as ex:
         # con.rollback()
         sse_resource_dict_error['error'] = ex
         sse_resource_dict_list = [sse_resource_dict_error, {}]
      finally:
         # con.close()
         return render_template("list.html",sse_resource_dict_list = sse_resource_dict_list)

if __name__ == '__main__':
   # run the web application on port 8080
    app.run(port=8080)
    
