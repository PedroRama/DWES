package com.example.myothercatalog;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PecesViewHolder extends RecyclerView.ViewHolder { //esto es para q me muestre el viewholder
    private TextView textView;
    private ImageView imageView;
    private PecesData titulo;

    public PecesViewHolder(@NonNull View itemView) { //esto es para q me muestre el itemview
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.txt_celda); //esto es para q me muestre el texto
        imageView = (ImageView) itemView.findViewById(R.id.img_celda); //

        itemView.setOnClickListener(new View.OnClickListener() {//esto es para q me muestre el onclick
            @Override
            public void onClick(View view) {
                String nombre = titulo.getName();   //esto es para q me muestre el nombre
                Context context = view.getContext(); //esto es para q me muestre el contexto
                Toast.makeText(context, "Clicaste en el titulo: " + nombre, Toast.LENGTH_LONG).show();//esto es para q me muestre el toast

                Intent intent = new Intent(context, Detail_Activity.class);//Aqui es donde se le pasa el contexto y la clase a la que se quiere ir

                intent.putExtra("titulo", titulo.getName());
                intent.putExtra("imagen", titulo.getImage_url());
                intent.putExtra("description", titulo.getDescription());

                context.startActivity(intent);
            }
        });
    }

    public void showData(PecesData data, Activity activity) { //esto es para q me muestre los datos
        this.textView.setText(data.getName()); //esto es para q me muestre el nombre
        Glide.with(itemView.getContext()).load(data.getImage_url()).into(this.imageView); //esto es para q me muestre la imagen
    }
}
