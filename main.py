from flask import Flask, render_template

app = Flask(__name__, template_folder='./')

JOBS = [{
  'id': 30,
  'title': 'Catering Supervisor',
  'location': 'SDSC,sriharikota,india',
  'salary': 50268
}, {
  'id': 31,
  'title': 'Nurse-B',
  'location': 'SDSC,sriharikota,india',
  'salary': 63758
}, {
  'id': 32,
  'title': 'Pharmacist-A',
  'location': 'SDSC,sriharikota,india',
  'salary': 41464
}, {
  'id': 33,
  'title': 'Radiographer-A',
  'location': 'SDSC,sriharikota,india',
  'salary': 36210
}, {
  'id': 34,
  'title': ' Lab Technician-A',
  'location': 'SDSC,sriharikota,india',
  'salary': 36210
}, {
  'id': 36,
  'title': 'Assistant',
  'location': 'SDSC,sriharikota,india',
  'salary': 36210
}, {
  'id': 37,
  'title': 'cook',
  'location': 'SDSC,sriharikota,india',
  'salary': 28258
}, {
  'id': 38,
  'title': 'light vehicle driver a',
  'location': 'SDSC,sriharikota,india',
  'salary': 28258
}, {
  'id': 39,
  'title': 'heavy vehicle driver a',
  'location': 'SDSC,sriharikota,india',
  'salary': 28258
}, {
  'id': 40,
  'title': 'fireman a',
  'location': 'SDSC,sriharikota,india',
  'salary': 28258
}, {
  'id': 41,
  'title': 'fireman a',
  'location': 'Vikram Sarabhai Space Centre (VSSC),Thiruvananthapuram',
  'salary': 28258
}, {
  'id': 42,
  'title': 'cook',
  'location': 'Vikram Sarabhai Space Centre (VSSC),Thiruvananthapuram',
  'salary': 30000
}, {
  'id': 43,
  'title': 'PG teacher',
  'location': 'Vikram Sarabhai Space Centre (VSSC),Thiruvananthapuram',
  'salary': 150000
}, {
  'id': 44,
  'title': 'trained graduate teacher',
  'location': 'Vikram Sarabhai Space Centre (VSSC),Thiruvananthapuram',
  'salary': 60000
}, {
  'id': 45,
  'title': 'junior transalation officer',
  'location': 'Vikram Sarabhai Space Centre (VSSC),Thiruvananthapuram',
  'salary': 30000
}, {
  'id': 46,
  'title': 'technitian b',
  'location': 'Space Applications Centre (SAC)',
  'salary': 150000
}, {
  'id': 47,
  'title': 'Draughtsman b',
  'location': 'Space Applications Centre (SAC)',
  'salary': 100000
}, {
  'id': 48,
  'title': 'Deputy/Assistant Director on Deputation basis',
  'location':
  'Indian National Space Promotion and Authorization Center (IN-SPACe), Ahmedabad',
  'salary': 200000
}, {
  'id': 49,
  'title': 'Junior Translation Officer',
  'location': 'Physical Research Laboratory (PRL) , Ahmedabad',
  'salary': 30000
}, {
  'id': 50,
  'title': 'library assistant a',
  'location': 'Physical Research Laboratory (PRL) , Ahmedabad',
  'salary': 15000
}, {
  'id': 51,
  'title': 'technical assiatant',
  'location': 'Liquid Propulsion Systems Centre (LPSC) , Bengaluru Ahmedabad',
  'salary': 35000
}, {
  'id': 52,
  'title': 'fireman a',
  'location': 'ISRO Propulsion Complex, Mahendragiri',
  'salary': 40000
}, {
  'id': 53,
  'title': 'technitian b',
  'location': 'Liquid Propulsion Systems Centre (LPSC) , Bengaluru',
  'salary': 150000
}, {
  'id': 54,
  'title': 'draughtsman b',
  'location': 'Liquid Propulsion Systems Centre (LPSC) , Bengaluru',
  'salary': 100000
}, {
  'id': 55,
  'title': 'Graduate and Technician Apprentices',
  'location': 'National Remote Sensing Centre (NRSC)',
  'salary': 40000
}, {
  'id': 56,
  'title': 'technical assistant',
  'location': 'U R Rao Satellite Centre (URSC) , Bengaluru',
  'salary': 35000
}, {
  'id': 57,
  'title': 'controller',
  'location': 'Human Space Flight Centre (HSFC)',
  'salary': 300000
}]


@app.route("/")
def home():
  return render_template('Templates/homepage.html', jobs=JOBS, company_name="careerleap")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  home()
