#from flask import Flask,render_template,request
import streamlit as st
import pickle 

model_dc = pickle.load(open('dc_bank_note.pkl','rb'))
model_ada = pickle.load(open('ada_bank_note.pkl','rb'))
model_rf = pickle.load(open('rf_bank_note.pkl','rb'))
model_lr = pickle.load(open('ls_bank_note.pkl','rb'))
model_kn = pickle.load(open('kn_bank_note.pkl','rb'))
model_sc = pickle.load(open('sc_bank_note.pkl','rb'))



#app =Flask(__name__)

#@app.route('/')
#def get_data():
	#return('This is dummy test for flask')

#@app.route('/stremlit_data')
def get_data_stream_lit():
	st.title('Prediction of the values using various Machine learning Alogorithm.')

	html_temp="""
	 <br></br>
	 <div style="background-color:cyan ; padding :10px">
	 </div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	activities =['Linear Regression','Decision Tree','Random forest', 'Ada Boost','Support Vector machine','Kn neighbor']
	option=st.sidebar.selectbox('which model you want to select?',activities)
	st.subheader(option)
	st.spinner('Hello')
	st_variance= st.slider('select the variance',-100,100)   
	st_skewness= st.slider('select the skewness',-100,100)
	st_curtosis= st.slider('select the curtosis',-100,100)
	st_entropy= st.slider('select the entropy',-100,100)

	inputs = [[st_variance,st_skewness,st_curtosis,st_entropy]]

	if st.button('Predict'):
		if option=='Linear Regression':
			st.success((model_lr.predict(inputs)[0]))
		elif option=='Ada Boost':
			st.success(((model_ada.predict(inputs)[0])))
		elif option=='Decision Tree':
			st.success(((model_dc.predict(inputs)[0])))
		elif option=='Random forest':
			st.success(((model_rf.predict(inputs)[0])))
		elif option=='Support Vector machine':
			st.success(((model_sc.predict(inputs)[0])))	
		else:
			st.success(((model_kn.predict(inputs)[0])))


if __name__=='__main__':
	#app.run(debug=True)
	get_data_stream_lit()