import 'package:flutter/material.dart';
import 'dart:math';

class Background extends StatefulWidget {
  const Background({Key? key}) : super(key: key);

  @override
  State<Background> createState() => _BackgroundState();
}

class _BackgroundState extends State<Background> {

  @override
  Widget build(BuildContext context) {
    return Center(
          child: Column (
            children: [
              Text("mooddddddddddd"),
              Container(
                width: MediaQuery.of(context).size.width,
                height: MediaQuery.of(context).size.height - 16,
                child: Center(
                  child: Container(
                    color: Colors.black,
                    width: MediaQuery.of(context).size.width / 5,
                    height: MediaQuery.of(context).size.width / 5,
                  )
                )
              )
            ]
          ),
    );
    
  }
}
