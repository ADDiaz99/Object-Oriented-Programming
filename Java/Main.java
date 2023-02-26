class Main {
    public static void main(String[] args) {
        System.out.println("Hola Java!");

        Car car = new Car("PES213", new Account("Pedro Perez", "pp12542154"));
        car.passenger = 4;
        car.printDataCar();
        System.out.println("Passengers: " + car.passenger);
        

        Car car_2 = new Car("AMS123", new Account("Clara Rojas", "Clar21656442"));
        car_2.passenger = 2;
        car_2.printDataCar();
        System.out.println("Passengers: " + car_2.passenger);
    }
    

}