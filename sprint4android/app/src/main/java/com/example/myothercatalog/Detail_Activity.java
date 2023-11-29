package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;
import com.bumptech.glide.Glide;

public class Detail_Activity extends AppCompatActivity{ //con el Detail_activity mostraremos el titulo, la imagen y la descripcion de lo que seleccionemos.
    private TextView NAME_PEZ;
    private ImageView IMG_PEZ;
    private TextView DESC_PEZ;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.detail_activity);

        Intent intent = getIntent();

        String titulo = getIntent().getStringExtra("titulo");
        String imagen = getIntent().getStringExtra("imagen");
        String description = getIntent().getStringExtra("description");

        viewDatos(titulo, imagen, description);
    }

    private void viewDatos(String titulo, String imagen, String description) {
        NAME_PEZ = findViewById(R.id.Name_pez);
        NAME_PEZ.setText(titulo);

        IMG_PEZ = findViewById(R.id.Img_pez);
        Glide.with(this).load(imagen).into(IMG_PEZ); //esto hace q se visualice la imagen

        DESC_PEZ = findViewById(R.id.Description_pez);
        DESC_PEZ.setText(description);
    }
}
