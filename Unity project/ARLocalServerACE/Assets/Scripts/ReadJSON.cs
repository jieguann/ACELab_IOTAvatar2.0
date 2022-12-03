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
    public Text TemperatureCText;
    public string TemperatureCVal;
    public Text TemperatureFText;
    public float TemperatureFVal;
    public Text LightText;
    public float lightVal;


	void Start()
	{
        Debug.Log("Test start");

        //string url = "http://192.168.4.1/ambientroom";//Connect to local server 192.168.0.13

        string url = "http://192.168.0.13/ambientroom";//Connect to local server 

        WWW www = new WWW(url);
        StartCoroutine(WaitForRequest(www));
       
	}
    IEnumerator WaitForRequest(WWW www){
        yield return www;
        if(www.error == null){

            Debug.Log("No error ...");
            
            Data = JsonMapper.ToObject(www.text);
            Debug.Log("Test Data is " + Data["temperature_c"][0]);
           //TemperatureCVal = Data["temperature_c"][0];



            //FOR DEBUG
            Debug.Log("Light:" + Data["light_brightness"][0]);
            Debug.Log("Temperature_c:" + Data["temperature_c"][0]);
            Debug.Log("Temperature_f:" +Data["temperature_f"][0]);
            Debug.Log("Humidity:" +Data["humidity"][0]);

        } else {
            Debug.Log("Error ...");
            Debug.Log("WWW Error:" + www.error);
        }

    }


	// Update is called once per frame
	void Update()
    {
        
    }
}
