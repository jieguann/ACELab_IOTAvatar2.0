using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class button : MonoBehaviour {
  //  private const string URL = "http://192.168.0.13/servo";
	public Text responseText;

	public void ServoRequest()
	{ 
		StartCoroutine (UploadServo());
	
	}
    public void LEDRequest()
    {
        StartCoroutine(UploadLED());

    }

	private IEnumerator UploadServo()
	{
        
        UnityWebRequest www = UnityWebRequest.Post(("http://192.168.0.13/servo"), "toggleServo");
		www.chunkedTransfer = false;////ADD THIS LINE
		yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("Form upload complete!");
        }

	}

    private IEnumerator UploadLED()
    {

        UnityWebRequest www = UnityWebRequest.Post(("http://192.168.0.13/led"), "toggleLED");
        www.chunkedTransfer = false;////ADD THIS LINE
        yield return www.SendWebRequest();

        if (www.isNetworkError || www.isHttpError)
        {
            Debug.Log(www.error);
        }
        else
        {
            Debug.Log("Form upload complete!");
        }

    }
}
