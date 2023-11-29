package com.example.myothercatalog;

import android.app.Activity;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;

public class PecesViewHolder extends RecyclerView.ViewHolder { //esto es para q me muestre el viewholder
    private final TextView textView;
    private final ImageView imageView;

    public PecesViewHolder(@NonNull View itemView) { //esto es para q me muestre el itemview
        super(itemView);
        textView = (TextView) itemView.findViewById(R.id.txt_celda); //esto es para q me muestre el texto
        imageView = (ImageView) itemView.findViewById(R.id.img_celda); //
    }

    public void showData(PecesData data, Activity activity) { //esto es para q me muestre los datos
        textView.setText(data.getName()); //esto es para q me muestre el nombre
        Glide.with(itemView.getContext()).load(data.getImage_url()).into(imageView); //esto es para q me muestre la imagen
    }
}
