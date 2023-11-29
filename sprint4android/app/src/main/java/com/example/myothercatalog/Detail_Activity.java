package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

public class Detail_Activity extends AppCompatActivity{ //con el Detail_activity mostraremos el titulo, la imagen y la descripcion de lo que seleccionemos.
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);
    }
}
