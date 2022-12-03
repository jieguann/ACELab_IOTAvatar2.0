using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class TextControl : MonoBehaviour
{
    public ReadFuzzy fuzzy;
    public TextMesh Emotion;
    

    // Start is called before the first frame update
    void Start()
    {
        fuzzy = fuzzy.GetComponent<ReadFuzzy>();
        Emotion = Emotion.GetComponent<TextMesh>();
        
    }

    // Update is called once per frame
    void Update()
    {
        Emotion.text = fuzzy.emotion;
        
    }
}
