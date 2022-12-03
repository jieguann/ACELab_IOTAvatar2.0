using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ParticleEnable : MonoBehaviour
{   public GameObject ParticleSad;
    public GameObject ParticleHappy;
    public GameObject ParticleAngry;
    public GameObject ParticleRelax;
    public GameObject ParticleNormal;

    // Start is called before the first frame update
    public void Start()
    {
        ParticleSad.SetActive(false);
        ParticleHappy.SetActive(false);
        ParticleAngry.SetActive(false);
        ParticleRelax.SetActive(false);
        ParticleNormal.SetActive(true);
    }


    public void TeSad()
    {
        ParticleSad.SetActive(true);
        ParticleHappy.SetActive(false);
        ParticleAngry.SetActive(false);
        ParticleRelax.SetActive(false);
        ParticleNormal.SetActive(false);
    }

    public void TeHappy()
    {
        ParticleHappy.SetActive(true);
        ParticleSad.SetActive(false);
        ParticleAngry.SetActive(false);
        ParticleRelax.SetActive(false);
        ParticleNormal.SetActive(false);

    }

    public void TeAngry()
    {
        ParticleSad.SetActive(false);
        ParticleHappy.SetActive(false);
        ParticleAngry.SetActive(true);
        ParticleRelax.SetActive(false);
        ParticleNormal.SetActive(false);
    }

    public void TeRelax()
    {
        ParticleHappy.SetActive(false);
        ParticleSad.SetActive(false);
        ParticleAngry.SetActive(false);
        ParticleRelax.SetActive(true);
        ParticleNormal.SetActive(false);

    }

    public void TeNormal()
    {
        ParticleHappy.SetActive(false);
        ParticleSad.SetActive(false);
        ParticleAngry.SetActive(false);
        ParticleRelax.SetActive(false);
        ParticleNormal.SetActive(true);

    }
}
