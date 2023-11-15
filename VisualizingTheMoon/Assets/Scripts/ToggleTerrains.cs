using System.Collections;
using System.Collections.Generic;
using Unity.VisualScripting;
using UnityEngine;

public class ToggleTerrains : MonoBehaviour
{
    public Terrain terrain;

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Alpha1))
        {
            toggle();
        } 
    }

    // Basically just bringing bottom layer to top everytime '1' is pressed
    private void toggle()
    {
        TerrainLayer[] layers = terrain.terrainData.terrainLayers;

        TerrainLayer[] newLayers = new TerrainLayer[layers.Length];

        newLayers[0] = layers[layers.Length - 1];

        for(int i = 0; i < layers.Length-1; i++)
        {
            newLayers[i+1] = layers[i];
        }

        terrain.terrainData.terrainLayers = newLayers;

        terrain.Flush();
    }
}
