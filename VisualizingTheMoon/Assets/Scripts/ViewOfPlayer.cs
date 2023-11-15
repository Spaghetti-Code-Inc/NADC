using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ViewOfPlayer : MonoBehaviour
{

    public Transform playerOreintation;
    // Update is called once per frame
    void Update()
    {
        transform.position = playerOreintation.position;
    }
}
