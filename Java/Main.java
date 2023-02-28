class Main {
    public static void main(String[] args) {
        System.out.println("Hola Java!");

        Car car = new Car("PES213", new Account("Pedro Perez","123456421","pedro@hotmail.com","5456784"));
        car.passenger = 4;
        car.printDataCar();
        System.out.println("Passengers: " + car.passenger);
        
    }
    

}