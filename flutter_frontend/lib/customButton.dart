import 'package:flutter/material.dart';

class CustomButton extends StatefulWidget {
  const CustomButton({Key? key}) : super(key: key);

  @override
  State<CustomButton> createState() => _CustomButtonState();
}

class _CustomButtonState extends State<CustomButton> {

  @override
  Widget build(BuildContext context) {
    return
      Center(
        child: OutlinedButton(
          child: Text("click for happiness"),
          onPressed: () {
            debugPrint('Received click');
          },
        )
    );
  }
}
