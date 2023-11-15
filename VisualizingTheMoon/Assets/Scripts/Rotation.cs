using System;
using UnityEditor;
using UnityEngine;

public class Rotation : MonoBehaviour
{
    // Rotates about 3200x3200 surface that is centered at (-1600, -1600) in xz plane

    public float rotationTime;
    private int radius = 3200;

    private double theta = 0;

    private float x;
    private float y = 1600;
    private float z;

    private Vector3 pos = new Vector3(-1600, 1600, 1600);

    private float xRot = 10;
    private float yRot;

    // Start is called before the first frame update
    void Start()
    {
        // Start position for camera everytime
        transform.position = pos;
    }

    // Update is called once per frame
    void Update()
    {
        theta += (rotationTime * Time.deltaTime);

        // X, Y, Z Coords
        // y is always 1600
        x = Convert.ToSingle(radius * Math.Sin(theta));
        z = Convert.ToSingle(radius * Math.Cos(theta));
        pos = new Vector3(x, y, z);
        transform.position = pos;


        // X, Y, Z Rotation
        transform.rotation = Quaternion.Euler(xRot, Convert.ToSingle((theta * (180.0 / Math.PI)) + 180 % 360), 0);


    }
}
