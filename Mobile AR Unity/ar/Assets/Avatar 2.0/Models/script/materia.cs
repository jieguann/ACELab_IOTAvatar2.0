using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class materia : MonoBehaviour
{
    public GameObject model;
    public Material happy;
    public Material sad;
    public Material normal;
    public Material relax;
    public Material angry;
    


    // Start is called before the first frame update
    void Start()
    {
        model.GetComponent<Renderer>().material = happy;


    }

    // Update is called once per frame
    /*void Update()
    {

        if (Input.GetKeyUp(KeyCode.Space))
        {
            model.GetComponent<Renderer>().material = happy;
        }

        if (Input.GetKeyDown(KeyCode.Space))
        {
            model.GetComponent<Renderer>().material = sad;
        }

    }
    */

    public void TeSad()
    {
        model.GetComponent<Renderer>().material = sad;
    }

    public void TeHappy()
    {
        model.GetComponent<Renderer>().material = happy;
    }
    public void TeNormal()
    {
        model.GetComponent<Renderer>().material = normal;
    }

    public void TeRelax()
    {
        model.GetComponent<Renderer>().material = relax;
    }
    public void TeAngry()
    {
        model.GetComponent<Renderer>().material = angry;
    }

}
