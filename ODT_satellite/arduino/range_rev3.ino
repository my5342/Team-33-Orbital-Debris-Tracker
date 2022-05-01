#include <Wire.h>
#include <Adafruit_ADS1015.h>
//-----------------------------------------------------
Adafruit_ADS1115 ads;
const float multiplier = 0.0001849F;

// the voltages
#define range_voltage (ads.readADC_SingleEnded(0))*multiplier
#define Ifreq_amplified_voltage (ads.readADC_SingleEnded(1))*multiplier-.2 
#define speed_voltage (ads.readADC_SingleEnded(2))*multiplier-.13
//-----------------------------------------------------

//-----------------------------------------------------
//initialize any variables
double current_particle_speed;
double temp_meas;
double range;
double myArray[5];
bool approach;
//-----------------------------------------------------


void setup() {
  Serial.begin(9600);
  ads.begin();
}

double range_equation(double voltage) {
  // [TODO]
  return 10-4.4*voltage;
}

double speed_equation(double voltage) {
  return voltage;
}

void loop() {
  double particle_speed = 0;
  bool check_for_approach = false;
  
  double max_voltage = 0;
  double min_voltage = 100;

  // start detecting a particle-----------------------------------------------
  while (speed_voltage > .1 && Ifreq_amplified_voltage > .15) {
    //find the maximum speed
    current_particle_speed = speed_voltage;
    if (current_particle_speed > particle_speed) { particle_speed = current_particle_speed;}
    
    //find if the particle is approaching or not
    if (!check_for_approach) {
      //1. get five measurements
      for (int i = 0; i < 6; i++) {myArray[i] = range_voltage;}
      //2. find if the particle is generally approaching or not
      int comp = 0;
      for (int i = 0; i < 5; i++) {
        if (myArray[i] < myArray[i+1]) { comp++; }
        else if (myArray[i] > myArray[i+1]) { comp--; }
      }
      approach = comp > 0;
      check_for_approach = true;
    }
    
    temp_meas = range_voltage;
    //update either the peak_voltage or the min voltage
    if (approach) {
      if (temp_meas > max_voltage) { max_voltage = temp_meas; }
    } else {
      if (temp_meas < min_voltage) { min_voltage = temp_meas; }
    }
  } //end of the while loop---------------------------------------------------

  //once the particle is gone---------------------------------------------------------
  //send the data to the rpi4
  if (particle_speed > .1) {
    if (check_for_approach) {
      if (approach) {
        range = range_equation(max_voltage);
        String retMe_position_x = "";
        retMe_position_x.concat(range);
  
        String retMe_velocity_y = "";
        retMe_velocity_y.concat(speed_equation(particle_speed));
        
        Serial.println(retMe_position_x + ",0" + ",0" + ",0" +","+retMe_velocity_y+",0");
      }
      else {
        range = range_equation(min_voltage);
        String retMe_position_x = "";
        retMe_position_x.concat(range);
  
        String retMe_velocity_y = "";
        retMe_velocity_y.concat(speed_equation(particle_speed));
        
        Serial.println(retMe_position_x + ",0" + ",0" + ",0" +",-"+retMe_velocity_y+",0");
      }
    }
  }
  //-----------------------------------------------------------------------------------
}
