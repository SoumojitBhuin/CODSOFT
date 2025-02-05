from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Dictionary to store contacts
contacts = {}

@app.route('/')
def index():
    
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    phone = request.form.get('phone')
    name = request.form.get('name')
    address = request.form.get('address')
    
    if phone and name and address:
        contacts[phone] = {'name': name, 'address': address}
    print(contacts)
    return render_template('index.html', contacts=contacts)

@app.route('/update', methods=['POST'])
def update_contact():
    phone = request.form.get('phone')
    name = request.form.get('name')
    address = request.form.get('address')
    
    if phone in contacts:
        contacts[phone] = {'name': name, 'address': address}
    print(contacts)
    return render_template('index.html', contacts=contacts)

@app.route('/delete/<int:contact_no>')
def delete_contact(contact_no):
    print(contact_no)
    
    if str(contact_no) in contacts.keys():
        print("true")
        del contacts[str(contact_no)]
    print(contacts)
    return render_template('index.html', contacts=contacts)

@app.route('/search', methods=['GET'])
def search_contact():
    query = request.args.get('query', '').lower()
    result = {phone: details for phone, details in contacts.items() 
              if query in phone or query in details['name'].lower()}
    
    return render_template('index.html', contacts=result)

if __name__ == '__main__':
    app.run(debug=True)
