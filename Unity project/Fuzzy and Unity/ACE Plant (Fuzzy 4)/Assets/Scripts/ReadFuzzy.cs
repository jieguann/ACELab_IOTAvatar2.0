using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using System.IO;
using System;
using LitJson;




public class ReadFuzzy : MonoBehaviour

{
    
    public string emotion;
    private JsonData Data;
    string url = "http://127.0.0.1:5000/";//Connect to local server, connect to python 'SentToHost'


    void Start()
    {
        Debug.Log("Test start");



        
        StartCoroutine(Read());
    }


    IEnumerator Read()
    {
        while (true)
        {
            WWW www = new WWW(url);
            


            yield return www;
          
            yield return new WaitForSeconds(0.2f);


            if (www.error == null)
            {

                Debug.Log("No error ...");
                //Getting Data From www
                Data = JsonMapper.ToObject(www.text);
               

                //FOR DEBUG

                //For Sensor
                Debug.Log("emotion:" + Data["emotion"]);

                emotion = Data["emotion"].ToString();


            }
            else
            {
                Debug.Log("Error ...");
                Debug.Log("WWW Error:" + www.error);
            }
        }
    }

}

///socket method not work well
/*
public string ipAdress = "127.0.0.1";

public int port = 1234;



private byte[] data = new byte[1024];

private Socket clientSocket;

private Thread receiveT;



void Start()

{

    ConnectToServer();

}



void ConnectToServer()

{

    try

    {

        clientSocket = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);

        clientSocket.Connect(IPAddress.Parse(ipAdress), port);

        Debug.Log("success");

        receiveT = new Thread(ReceiveMsg);

        receiveT.Start();



    }

    catch (System.Exception ex)

    {

        Debug.Log("fail to connect！");

        Debug.Log(ex.Message);

    }

}



private void ReceiveMsg()

{

    while (true)

    {

        if (clientSocket.Connected == false)

        {

            Debug.Log("fail");

            break;

        }



        int lenght = 0;

        lenght = clientSocket.Receive(data);



        string str = Encoding.UTF8.GetString(data, 0, data.Length);



        emotion = str;


    }

}


void OnDestroy()

{

    try

    {

        if (clientSocket != null)

        {

            clientSocket.Shutdown(SocketShutdown.Both);

            clientSocket.Close();

        }



        if (receiveT != null)

        {

            receiveT.Interrupt();

            receiveT.Abort();

        }



    }

    catch (Exception ex)

    {

        Debug.Log(ex.Message);

    }

}
*/


