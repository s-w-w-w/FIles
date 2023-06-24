#!/usr/bin/env python3

import sys
from pathlib import Path
# add parent path of lib dir to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest

# display path
from lib.Files import *

class TestFiles(unittest.TestCase): 

    """
    test file1.txt
    """
    def test_something(self):
      filePath=Path(__file__).resolve().parent.parent / "files/file1.txt"
      if os.path.exists(filePath):
        Path.unlink(filePath)
      
      fs = Files(filePath)
      self.assertEqual(True,fs.exists())
      self.assertEqual([],fs.get())
      fs.append('first line')
      fs.append('second line')
      self.assertEqual(['first line\n','second line\n'],fs.get())
      fs.append('third line')
      self.assertEqual(['first line\n','second line\n','third line\n'],fs.get())
      self.assertEqual(3,len(fs.get()))
      fs.clear()
      self.assertEqual([],fs.get())
      self.assertEqual(0,len(fs.get()))
      fs.append('first line')
      fs.append('second line')
      self.assertEqual(['first line\n','second line\n'],fs.get())
      fs.removeOne(1);
      self.assertEqual(['first line\n'],fs.get())
      fs.update(0,"New first task");
      self.assertEqual(['New first task\n'],fs.get())
      fs.supplement(0,"complete");
      self.assertEqual(['New first task complete\n'],fs.get())
      fs.delete()
      self.assertEqual(False,fs.exists())

if __name__ == '__main__':
    unittest.main()

