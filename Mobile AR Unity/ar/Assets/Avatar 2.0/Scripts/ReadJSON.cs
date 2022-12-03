using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using System;
using LitJson;

public class ReadJSON : MonoBehaviour
{

    private JsonData Data;
    private JsonData Datap;

    public float TemperatureCVal;
  
    public float TemperatureFVal;
  
    public float lightVal;

    public float humidity;

    public string STem_C;
    public string STem_F;
    public string Slight;
    public string Shumidity;

    public string PeoplePresent;
    public int CountPeople;
   
    



    private IEnumerator Sensor;
   

    string url = "http://192.168.0.13/ambientroom";//Connect to local server 
    string Peopleurl = "http://192.168.0.4:5100/detection";//Connect to Raspeberry Pi(people Presence)

    void Start()
    {
        Debug.Log("Test start");

       
        
        Sensor = SensorIn();
        StartCoroutine(Sensor);

    




    }



    IEnumerator SensorIn()
    {
        while (true)
        {
            WWW www = new WWW(url);
            WWW wwwp = new WWW(Peopleurl);


            yield return www;
            yield return wwwp;
            yield return new WaitForSeconds(0.2f);


            if (www.error == null)
            {

                Debug.Log("No error ...");
                //Getting Data From www
                Data = JsonMapper.ToObject(www.text);
                Datap= JsonMapper.ToObject(wwwp.text);

                //FOR DEBUG

                //For Sensor
                Debug.Log("Light:" + Data["light_brightness"][0]);
                Debug.Log("Temperature_c:" + Data["temperature_c"][0]);
                Debug.Log("Temperature_f:" + Data["temperature_f"][0]);
                Debug.Log("Humidity:" + Data["humidity"][0]);
                Debug.Log("Motion:" + Data["motion_detected"]);

                //For people present
                Debug.Log(Datap["people"]);
                
                Debug.Log(Datap["count"]);
                
                //For Save File
                SaveFile(Data["light_brightness"][0].ToString(), Data["temperature_c"][0].ToString(), Data["temperature_f"][0].ToString());



                //For Json to float
                GetJsonFloat(Single.Parse(Data["temperature_c"][0].ToString()), Single.Parse(Data["temperature_f"][0].ToString()),
                    Single.Parse(Data["light_brightness"][0].ToString()), Single.Parse(Data["humidity"][0].ToString()),int.Parse(Datap["count"].ToString()));
                // Json to String
                GetJsonString(Data["temperature_c"][0].ToString(), Data["temperature_f"][0].ToString(), 
                    Data["light_brightness"][0].ToString(), Data["humidity"][0].ToString(), Datap["people"].ToString());
            }
            else
            {
                Debug.Log("Error ...");
                Debug.Log("WWW Error:" + www.error);
            }
        }
    }


   


    //Get Json Float
    public void GetJsonFloat(float Tem_c, float Tem_f, float Light, float Humidity, int People)
    {
        TemperatureCVal = Tem_c;
           lightVal = Light;
        TemperatureFVal = Tem_f;
        humidity = Humidity;
        CountPeople = People;
       
    }
    //Get Json String 
    public void GetJsonString(string Tem_c, string Tem_f, string Light, string Humidity, string People)
    {
        STem_C = Tem_c;
        STem_F=Tem_f;
         Slight= Light;
    Shumidity= Humidity;
       PeoplePresent = People;
  
}


    //Save File
    public void SaveFile(string b, string t, string h)
    {

        string destination = Application.persistentDataPath + "/save.txt";



        using (StreamWriter w = File.AppendText(destination))
        {
            w.WriteLine(b + "," + t + "," + h);
        }

    }
  
}
