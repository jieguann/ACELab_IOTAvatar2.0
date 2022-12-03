using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Position : MonoBehaviour
{   public Transform plantAvatar;
    public Transform leftControler;
    public Transform rightControler;
    // Start is called before the first frame update
    void Start()
    {
        plantAvatar.transform.SetParent(leftControler);
        plantAvatar.transform.position = new Vector3(leftControler.transform.position.x, leftControler.transform.position.y,leftControler.transform.position.z);

    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void toRightControler()
    {
        plantAvatar.transform.SetParent(rightControler);
        plantAvatar.transform.position = new Vector3(rightControler.transform.position.x, rightControler.transform.position.y, rightControler.transform.position.z);
    }

    public void toLeftControler()
    {
        plantAvatar.transform.SetParent(leftControler);
        plantAvatar.transform.position = new Vector3(leftControler.transform.position.x, leftControler.transform.position.y, leftControler.transform.position.z);
    }
}
