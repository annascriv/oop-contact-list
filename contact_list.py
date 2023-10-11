class ContactList:


    def __init__(self, name, contacts):
        self.name = name
        self.contacts = contacts

    def __str__(self):
        return f"{self.name} : {self.contacts}"
    
    @property
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name

    @property
    def get_contacts(self):
        return self.contacts
    
    @get_contacts.setter
    def set_contacts(self, new_list):
        self.contacts = new_list


    
    def add_contact(self, new_contact):
        self.contacts.append(new_contact)

    def remove_contact(self, name):
        
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)

    def find_shared_contacts(self, list):
        shared_contacts = []

        for contact in self.contacts:
            for name in list.contacts:
                if name == contact:
                    shared_contacts.append(name)
        return shared_contacts








        
    