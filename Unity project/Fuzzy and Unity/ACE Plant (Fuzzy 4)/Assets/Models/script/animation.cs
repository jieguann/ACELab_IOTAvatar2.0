using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class animation : MonoBehaviour
{
    public Animator anim;
    // Start is called before the first frame update
    void Start()
    {
        anim = anim.GetComponent<Animator>();
    }

    // Update is called once per frame
  

    public void Sad()
    {
        anim.SetTrigger("sad");
    }

    public void Happy()
    {
        anim.SetTrigger("dance");
    }

    public void Sleep()
    {
        anim.SetTrigger("sleep");
    }

    public void Normal()
    {
        anim.SetTrigger("normal");
    }

    public void Angry()
    {
        anim.SetTrigger("angry");
    }
}
