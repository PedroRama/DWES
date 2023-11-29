package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class PecesData {
    private String name;
    private String image_url;

    public PecesData(JSONObject json) {
        try{
            this.name = json.getString("name");//esto es para q me muestre el nombre
            this.image_url = json.getString("image_url");//esto es para q me muestre la imagen
        }catch (JSONException e) {
            e.printStackTrace(); //esto es para q si hay un error me lo muestre
        }
    }

    public String getName() {
        return name;
    }
    public String getImage_url() {
        return image_url;
    }


}
