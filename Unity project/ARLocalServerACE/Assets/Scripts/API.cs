using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class API : MonoBehaviour {

    private const string URL = "http://192.168.4.1/ambientroom";
    public Text responseText;

    public void Request(){
        WWWForm form = new WWWForm();
        Dictionary<string, string> headers = form.headers;
        WWW request = new WWW(URL,null,headers);
        StartCoroutine(ONReponse(request));

    }
    private IEnumerator ONReponse(WWW req){
        yield return req;
        responseText.text = req.text;
    }
}
