using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class CircleGenerator : MonoBehaviour
{
    [SerializeField] GameObject CubePrefab;
    [SerializeField] InputField RadiusInput;
    [SerializeField] GameObject Plane;
    GameObject CircleParent;
    Renderer PlaneRenderer;

    private void Start(){
        CircleParent = new GameObject("CircleParent");
        PlaneRenderer = Plane.GetComponent<Renderer>();
    }

    public void OnEnterButton()
    {
        if (RadiusInput.text.Length > 0)
        {
            int CircleRadius = int.Parse(RadiusInput.text);
            CircleRadius = Mathf.Abs(CircleRadius);
            Destroy(CircleParent);
            Generate(CircleRadius);
        }
    }

    void Generate(int Radius)
    {
        CircleParent = new GameObject("CircleParent");
        int RadiusSquared = Radius * Radius;

        int OldPosZ = 0;
        int NewZPos;

        for (int x = -Radius; x <= Radius; x++)
        {
            float RawHeightX = Mathf.Sqrt(RadiusSquared - x * x);
            int HeightX = Mathf.RoundToInt(RawHeightX);

            Instantiate(CubePrefab, new Vector3(x, 0, HeightX), Quaternion.identity, CircleParent.transform);
            if (HeightX > 0){
                Instantiate(CubePrefab, new Vector3(x, 0, -HeightX), Quaternion.identity, CircleParent.transform);}
            

            NewZPos = HeightX;
            if (Mathf.Abs(OldPosZ - NewZPos) > 1)
            {
                int Step; //Positive or Negative
                int Start;
                int Stop;
                if (NewZPos > OldPosZ)
                {
                    Step = 1;
                    Start = OldPosZ;
                    Stop = NewZPos;}
                else{
                    Step = -1;
                    Start = NewZPos;
                    Stop = OldPosZ;
                }
                for (int y = Start + 1; y < Stop; y++)
                {
                    float RawHeightx = Mathf.Sqrt(RadiusSquared - y * y) * -Step;
                    int Heightx = Mathf.RoundToInt(RawHeightx);
                    Instantiate(CubePrefab, new Vector3(Heightx, 0, y), Quaternion.identity, CircleParent.transform);
                    Instantiate(CubePrefab, new Vector3(Heightx, 0, -y), Quaternion.identity, CircleParent.transform);
                }
            }

            OldPosZ = HeightX;
        }

        float ScaleDivider = 1 + Radius;
        CircleParent.transform.localScale = new Vector3(1 / ScaleDivider, 1, 1 / ScaleDivider);
        PlaneRenderer.material.mainTextureScale = new Vector2(10 * (1 + Radius), 10 * (1 + Radius));
        Batch(CircleParent);
    }

    public static void Batch(GameObject Parent)
    {
        StaticBatchingUtility.Combine(Parent);
    }
}
