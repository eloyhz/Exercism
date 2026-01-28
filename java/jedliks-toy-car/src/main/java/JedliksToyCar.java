public class JedliksToyCar {
    private int distance;
    private int battery;

    public JedliksToyCar()  {
        this.distance = 0;
        this.battery = 100;
    }

    public static JedliksToyCar buy() {
        JedliksToyCar car = new JedliksToyCar();
        return car;
    }

    public String distanceDisplay() {
        return "Driven " + this.distance + " meters";
    }

    public String batteryDisplay() {
        if (this.battery == 0)  {
            return "Battery empty";
        }
        else    {
            return "Battery at " + this.battery + "%";
        }
    }

    public void drive() {
        if (this.battery > 0)   {
            this.distance += 20;
            this.battery--;
        }
    }
}
