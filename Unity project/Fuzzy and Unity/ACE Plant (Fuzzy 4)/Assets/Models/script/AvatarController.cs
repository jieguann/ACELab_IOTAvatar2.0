using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Events;
public class MyIntEvent : UnityEvent<int>
{
}

public class AvatarController : MonoBehaviour
{
    public ReadFuzzy fuzzy;

    public UnityEvent ToSad;
    public UnityEvent ToRelaxation;
    public UnityEvent ToHappy;
    public UnityEvent ToAngry;
    public UnityEvent ToNeutral;
    public string emotion;


    private void Start()
    {
        fuzzy = fuzzy.GetComponent<ReadFuzzy>();
       
    }

    void Update()

    {
        emotion = fuzzy.emotion;

        //print(emotion.GetType());

        //print("r".GetType());
        //print(emotion);
        //Debug.Log("relaxation".Equals(emotion));
        //Debug.Log(string.Compare(emotion, "r", true));


        if (emotion.Equals("sad") == true) Sad();

        else if (emotion.Equals("relaxation") == true) Relaxation();


        else if (emotion.Equals("happy") == true) Happy();

        else if (emotion.Equals("angry") == true) Angry();

        else if (emotion.Equals("normal") == true) Neutral();

        else Neutral();
     

    }

    void Sad()
    {
        
        ToSad.Invoke();
    }

    void Relaxation()
    {

        ToRelaxation.Invoke();
    }

    void Happy()
    {
       ToHappy.Invoke();
    }

    void Angry()
    {
        ToAngry.Invoke();
    }

    void Neutral()
    {
        ToNeutral.Invoke();
    }

}
