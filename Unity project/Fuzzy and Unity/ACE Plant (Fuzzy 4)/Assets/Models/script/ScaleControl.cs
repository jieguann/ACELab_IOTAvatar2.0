using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScaleControl : MonoBehaviour
{
    public Transform Plant;
    // Start is called before the first frame update
    void Start()
    {
        Plant = Plant.GetComponent<Transform>();
        Plant.localScale = new Vector3(0.03794428f, 0.03794428f, 0.03794428f);
    }

public void Tonormal()
    {
        Plant.localScale = new Vector3(0.03794428f, 0.03794428f, 0.03794428f);
    }

  public void ToBig()
    {
        Plant.localScale = new Vector3(0.4f, 0.4f, 0.4f);
    }
}
