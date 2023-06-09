public class CarsAssemble {

    public double productionRatePerHour(int speed) {
        if(speed > 9) {
            return 221*speed*0.77;
        }
        else if(speed > 8) {
            return 221*speed*0.8;
        }
        else if(speed > 4) {
            return 221*speed*0.9;
        }
        else {
            return 221*speed;
        }
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed)/60;
    }
}
