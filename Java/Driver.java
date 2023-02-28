class Driver extends Account{
    public Driver(String name, String document, String email, String password){
        super(name, document);

    }

    void printDataUser(){
        System.out.println("Name: " + name + " Document: " + document + " E-mail: " + email + " Password: " + password);
    }
    
}
